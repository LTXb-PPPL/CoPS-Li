program source_ref
	use mods
	implicit none
	include 'mpif.h'
!----------------------------------------------------------------------------------
	integer ierr, nprocs,resultlen, rank
	real, dimension(:,:,:), allocatable :: pq
	real, dimension(:,:), allocatable :: d, tq
	real, dimension(:,:), allocatable :: dep_rank
	real, dimension(:,:), allocatable :: t_x, t_y, t_z, t_n, t_c, tc_ch, tn_ch, tx_ch, ty_ch, tz_ch
	real, dimension(:,:), allocatable :: obs_c, obs_n
	real, dimension(:,:), allocatable :: fr_x, fr_y, fr_z, fr_n, fr_c, r_x, r_y, r_z, r_n, r_c
	real, dimension(:,:), allocatable :: ro_x, ro_y, ro_z, ro_n, ro_c
	real, dimension(:,:), allocatable :: thickness, obs_p1, obs_p2, obs_p3
	integer, dimension(:), allocatable :: orientation,check_obs
	real, dimension(:), allocatable :: dep, t
	integer :: i,n_s,n_r,n_t,n_o, io_op,io_diag,k,start,end,n_s_r0,remainder,chunks,nt_ch,targets,j,sources
	CHARACTER(100) :: geo_path
	character(100) :: hname,geo_name,sname,rname,so_name,ro_name
	INTEGER DATE_TIME (8)
	CHARACTER (LEN = 12) REAL_CLOCK (3)
	integer status(MPI_STATUS_SIZE)
	real :: startTime, stopTime

!----------------------------------------------------------------------------------
!				Initiate Run
!----------------------------------------------------------------------------------	
	CALL DATE_AND_TIME (REAL_CLOCK (1), REAL_CLOCK (2), &
                    REAL_CLOCK (3), DATE_TIME)

	call mpi_init(ierr)
	call mpi_get_processor_name(hname, resultlen, ierr)
	call MPI_COMM_SIZE(MPI_COMM_WORLD,nprocs,ierr)
	call MPI_COMM_RANK(MPI_COMM_WORLD,rank,ierr)
	geo_path = '/p/ltxdata/Li_evporator/Li_Evap_Source/Fortran_Source/CAD_Source/geom_mark2'
	!geo_path = '/p/ltxdata/Li_evporator/test_geom'
	geo_name = "target"

	rname = "reflector"
	so_name = "obs_source"
	ro_name = "obs_reflector"

!----------------------------------------------------------------------------------
	! read targets 
	call read_geometry(geo_path, geo_name, t_x, t_y, t_z, t_n, t_c)
	call read_geometry(geo_path, rname, fr_x, fr_y, fr_z, fr_n, fr_c)
	call read_geometry(geo_path, ro_name, ro_x, ro_y, ro_z, ro_n, ro_c)
	!print *, 'read ok'
	allocate(r_x(n_r,3),r_y(n_r,3),r_z(n_r,3),r_n(n_r,3),r_c(n_r,3))



	call MPI_BARRIER(MPI_COMM_WORLD,ierr)
	n_r = size(fr_x,1)/nprocs
	remainder = modulo(size(fr_x,1),nprocs)
	if (rank < remainder) then
		start = rank*(n_r+1)+1
		end = start + n_r
	else
		start = rank*n_r + remainder +1 
		end = start + n_r - 1
	end if

	r_x = fr_x(start:end,:)
	r_y = fr_y(start:end,:)
	r_z = fr_z(start:end,:)
	r_n = fr_n(start:end,:)
	r_c = fr_c(start:end,:)
	sources = size(r_c,1)

	!print*, "rank = ", rank, " n_s = ", n_s, " n_r = ", n_r
	call MPI_BARRIER(MPI_COMM_WORLD,ierr)
	if (rank == 0) then
		io_op = 17
		io_diag = 18
		open(io_diag, file='diagnostics.txt', status='replace', action='write')
		open(io_op, file='LTX_R0.txt', status='replace', action='write')
	end if



!----------------------------------------------------------------------------------
! check orientation of sources against targets
!----------------------------------------------------------------------------------
	!do i=1,n_s
	!	print*, "rank = ", rank, 'i = ', i, s_c(i,:)
	!end do
	n_t = size(t_x,1)
	n_o = n_t+size(ro_x,1)
	allocate(obs_c(n_o,3),obs_n(n_o,3),obs_p1(n_o,3),obs_p2(n_o,3),obs_p3(n_o,3))
	obs_c(1:n_t,:) = t_c
	obs_n(1:n_t,:) = t_n
	obs_c(n_t+1:n_o,:) = ro_c
	obs_n(n_t+1:n_o,:) = ro_n	

	obs_p1(1:n_t,1) = t_x(:,1)
	obs_p1(1:n_t,2) = t_y(:,1)
	obs_p1(1:n_t,3) = t_z(:,1)
	obs_p2(1:n_t,1) = t_x(:,2)
	obs_p2(1:n_t,2) = t_y(:,2)
	obs_p2(1:n_t,3) = t_z(:,2)
	obs_p3(1:n_t,1) = t_x(:,3)
	obs_p3(1:n_t,2) = t_y(:,3)
	obs_p3(1:n_t,3) = t_z(:,3)
	obs_p1(n_t+1:n_o,1) = ro_x(:,1)
	obs_p1(n_t+1:n_o,2) = ro_y(:,1)
	obs_p1(n_t+1:n_o,3) = ro_z(:,1)
	obs_p2(n_t+1:n_o,1) = ro_x(:,2)
	obs_p2(n_t+1:n_o,2) = ro_y(:,2)
	obs_p2(n_t+1:n_o,3) = ro_z(:,2)
	obs_p3(n_t+1:n_o,1) = ro_x(:,3)
	obs_p3(n_t+1:n_o,2) = ro_y(:,3)
	obs_p3(n_t+1:n_o,3) = ro_z(:,3)

	chunks = 233

	!print *, 'target divided in to chunks = ', chunk
	nt_ch = size(t_x,1)/chunks
	!print *, 'nt_ch - ', nt_ch

	do j = 1, chunks
		!call cpu_time(startTime)
		if (j < chunks) then
			if (rank == 0) then
				print*, "rank = ", rank, " chunk = ", j, " start = ", (j-1)*nt_ch+1, " end = ", j*nt_ch
			end if
			tn_ch = t_n((j-1)*nt_ch+1:j*nt_ch,:)
			tc_ch = t_c((j-1)*nt_ch+1:j*nt_ch,:)
		else
			if (rank == 0) then
				print*, "rank = ", rank, " chunk = ", j, " start = ", (j-1)*nt_ch+1, " end = ", size(t_x,1)
			end if
			tn_ch = t_n((j-1)*nt_ch+1:size(t_x,1),:)
			tc_ch = t_c((j-1)*nt_ch+1:size(t_x,1),:)
		end if
		targets = size(tn_ch,1)

		allocate(orientation(targets))
		allocate(d(targets,3),t(targets))
		allocate(pq(targets,n_o,3),tq(targets,n_o))
		allocate(check_obs(targets))
		allocate(thickness(sources,targets))
		thickness = 0.0
	!----------------------------------------------------------------------------------

		do i=1,sources
			
			call check_orientation(io_diag,rank,tn_ch,tc_ch,r_n(i,:),r_c(i,:),orientation)

			
			call calc_dt(io_diag,rank,r_c(i,:),tc_ch,d,t)

			
			call get_q(io_diag,rank,r_c(i,:),r_n(i,:),obs_c,obs_n,d,t,pq,tq)

			
			call check_obstruction(io_diag,rank,r_c(i,:),r_n(i,:),d,t,pq,tq,obs_p1,obs_p2,obs_p3,check_obs)

			call get_deposition(size(fr_x,1),rank,r_c(i,:),r_n(i,:),d,t,tn_ch,orientation,check_obs,thickness(i,:))

			
		end do
	!----------------------------------------------------------------------------------
		allocate(dep(targets))
		dep = sum(thickness,dim=1)
		call MPI_BARRIER(MPI_COMM_WORLD,ierr)



	!----------------------------------------------------------------------------------
	!				collect thickness to rank=0
	!----------------------------------------------------------------------------------
		


		if (rank .NE. 0) then 
			! send dep and thickness to rank 0
			!print*, "rank = ", rank, " sending"
			call MPI_SEND(dep,targets,MPI_REAL,0,rank,MPI_COMM_WORLD,ierr)
			!call MPI_SEND(dep,targets,MPI_REAL,0,rank,MPI_COMM_WORLD,ierr)
		end if
		
		!print*, "rank = ", rank, " finished sending"
		if (rank == 0) then
			allocate(dep_rank(nprocs-1,targets))
			do i = 1,nprocs-1
				call MPI_RECV(dep_rank(i,:),targets,MPI_REAL,i,i,MPI_COMM_WORLD,status,ierr)
				!print*, "rank = ", rank, " finished receiving from ", i
			end do
			dep = dep + sum(dep_rank,dim=1)
			! create output file and write deposition
			!print*, "rank = ", rank, " writing to file"
			do k=1,targets
				!print*, dep(k), t_n(k,1), t_n(k,2), t_n(k,3)
				write(io_op,*) (j-1)*nt_ch+k, dep(k), tn_ch(k,1), tn_ch(k,2), tn_ch(k,3)
			end do
			!print*, "rank = ", rank, " finished writing to file", " for chunk ", j
			deallocate(dep_rank)
			close(io_diag)
		end if
		!call cpu_time(stopTime)
		!write(*, '(A, F8.6)') 'Elapsed time, s : ',  (stopTime - startTime), ' seconds', ' for chunk ', j
		call MPI_BARRIER(MPI_COMM_WORLD,ierr)
		deallocate(orientation,d,t,pq,tq,check_obs,thickness,dep)
	end do
	deallocate(t_x,t_y,t_z,t_n,t_c,fr_x,fr_y,fr_z, &
	fr_n,fr_c,r_x,r_y,r_z,r_n,r_c,ro_x,ro_y,ro_z,ro_n,ro_c,obs_c,obs_n, &
	obs_p1,obs_p2,obs_p3)
	close(io_op)
!----------------------------------------------------------------------------------
!				End Run
!----------------------------------------------------------------------------------
	call MPI_BARRIER(MPI_COMM_WORLD,ierr)
	call mpi_finalize(ierr)
end program source_ref

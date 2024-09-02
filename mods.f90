module mods
implicit none

contains

    subroutine read_geometry(geo_path, geo_name, x, y, z, norm, centroid)
        character(len=100), intent(in) :: geo_path, geo_name
        real, dimension(:,:), allocatable, intent(out) :: x, y, z, norm, centroid
        integer :: i, j, n, ierr,io
        character(len=500) :: fname
        real :: temp
        
        ! read x
        fname = trim(geo_path)//'/'//trim(geo_name)//'.x.DAT'
        open(10, file=fname, status='old', action='read')
        n = 0
        do
        	read(10,*,iostat=io) 
        	if (io /= 0) exit
        	n = n + 1
        end do
        allocate(x(n,3))
        rewind(10)
        do i=1,n
        	read(10,*) x(i,1), x(i,2), x(i,3)
        end do
        close(10)

        ! read y
        fname = trim(geo_path)//'/'//trim(geo_name)//'.y.DAT'
        open(10, file=fname, status='old', action='read')
        
        allocate(y(n,3))
        do i=1,n
        	read(10,*) y(i,1), y(i,2), y(i,3)
        end do
        close(10)
        
        ! read z
        fname = trim(geo_path)//'/'//trim(geo_name)//'.z.DAT'
        open(10, file=fname, status='old', action='read')
        
        allocate(z(n,3))
        do i=1,n
        	read(10,*) z(i,1), z(i,2), z(i,3)
        end do
        close(10)
        
        ! read norm
        fname = trim(geo_path)//'/'//trim(geo_name)//'.norm.DAT'
        open(10, file=fname, status='old', action='read')
        
        allocate(norm(n,3))
        do i=1,n
        	read(10,*) norm(i,1), norm(i,2), norm(i,3)
        end do
        close(10)
        
        ! read centroid
        fname = trim(geo_path)//'/'//trim(geo_name)//'.centroids.DAT'
        open(10, file=fname, status='old', action='read')
        
        allocate(centroid(n,3))
        do i=1,n
        	read(10,*) centroid(i,1), centroid(i,2), centroid(i,3)
        end do
        close(10)
        return
    end subroutine read_geometry


    subroutine check_orientation(io, rank, t_n, t_c, source_n, source_c, orientation)
        real, dimension(:,:), intent(in) :: t_n, t_c
        real, dimension(:), intent(in) :: source_n, source_c
        integer, dimension(:), intent(out) :: orientation
        real, dimension(:), allocatable :: ts, st
        real, dimension(:,:), allocatable :: dummy_c, dummy_n
        integer, intent(in) :: rank, io
        integer :: n_t, k
        real :: temp
        n_t = size(t_n,1)
        allocate(ts(n_t),st(n_t))
        allocate(dummy_c(n_t,3),dummy_n(n_t,3))
        !print *, "size(t_n,1) = ", size(t_n,1)
        dummy_c = spread(source_c,1,size(t_n,1))
        ts = sum((dummy_c-t_c)*t_n,dim=2)
        dummy_n = spread(source_n,1,size(t_n,1))
        st = sum((t_c-dummy_c)*dummy_n,dim=2)
        ! if st and ts are both positive, then the orientation is correct
        orientation = 0
        do k = 1,n_t
            if (ts(k) > 0 .and. st(k) > 0) then
                orientation(k) = 1
            end if
        end do

        deallocate(ts,st,dummy_c,dummy_n)
    end subroutine check_orientation

    subroutine calc_dt(io,rank, source_c, target_c, d, t)
        real, dimension(:,:), intent(in) :: target_c
        real, dimension(:,:), intent(inout) :: d
        real, dimension(:), intent(in) :: source_c
        real, dimension(:), intent(out) :: t
        integer, intent(in) :: rank, io
        real, dimension(:,:), allocatable :: dummy_c, dummy_d
        integer :: n_t
        real :: temp
        n_t = size(target_c,1)
        allocate(dummy_c(n_t,3),dummy_d(n_t,3))
        dummy_c = spread(source_c,1,n_t)
        t = norm2(target_c-dummy_c,dim=2)
        dummy_d = target_c - dummy_c
        d(:,1) = (dummy_d(:,1)/t)
        d(:,2) = (dummy_d(:,2)/t)
        d(:,3) = (dummy_d(:,3)/t)
        deallocate(dummy_c,dummy_d)
    end subroutine calc_dt

    subroutine get_q(io,rank,s,sn,obs_c,obs_n,d,t,pq,tq)
        real, dimension(:), intent(in) :: s,sn,t
        real, dimension(:,:), intent(in) :: d,obs_c,obs_n
        real, dimension(:,:,:), intent(out) :: pq
        real, dimension(:,:), intent(out) :: tq
        integer, intent(in) :: rank, io
        real, dimension(:,:), allocatable :: den
        real, dimension(:), allocatable :: num
        integer ::  n_o, n_t, k, j
        real :: temp
        n_o = size(obs_c,1)
        n_t = size(t)
        allocate(num(n_o),den(n_t,n_o))
        num = sum(obs_c*obs_n,dim=2) - sum(obs_n*spread(s,1,n_o),dim=2)
        do k=1,n_t
        	den(k,:) = sum(obs_n*spread(d(k,:),1,n_o),dim=2)
        end do
        tq = spread(num,1,n_t)/den  

      	do k = 1,n_t
            do j = 1,n_o
                pq(k,j,:) = d(k,:)*tq(k,j) + s
            end do
        end do
        deallocate(num,den)      
    end subroutine get_q

    subroutine check_obstruction(io,rank,s,sn,d,t,pq,tq,p1,p2,p3,checkobs)
        real, dimension(:), intent(in) :: s,sn,t
        real, dimension(:,:), intent(in) :: d,tq,p1,p2,p3
        real, dimension(:,:,:), intent(in) :: pq
        integer, dimension(:), intent(inout) :: checkobs
        integer, intent(in) :: rank, io
        real, dimension(:,:), allocatable :: dummy_dist, uv, wu
        real, dimension(:,:,:), allocatable :: u,v,w, p1q,p2q,p3q
        integer, dimension(:,:), allocatable :: distance, cond
        real, dimension(:,:,:), allocatable :: p1T, p2T, p3T
        integer :: n_o, n_t, k, j

        n_o = size(p1,1)
        n_t = size(t)


        !if (rank == 0 .and. i==1) then
        !    print *, "p1 = ", p1(1,:), "p2 = ", p2(1,:), "p3 = ", p3(1,:)    
        !end if

        allocate(p1q(n_t,n_o,3),p2q(n_t,n_o,3),p3q(n_t,n_o,3))
        allocate(u(n_t,n_o,3),v(n_t,n_o,3),w(n_t,n_o,3))
        ! subtract p1 from pq, but p1 needs to be the same size as pq
        !allocate(p1T(n_t,n_o,3),p2T(n_t,n_o,3),p3T(n_t,n_o,3))
        ! each column of p1T is p1 repeated n_t times
        allocate(wu(n_t,n_o),uv(n_t,n_o))
        allocate(cond(n_t,n_o))
        allocate(dummy_dist(n_t,n_o),distance(n_t,n_o))
        cond = 0
        checkobs = 0
        do k = 1,n_t
            do j = 1,n_o
                !p1T(k,j,:) = p1(j,:)
                !print *, "p1(j,:) = ", p1(j,:)
                !p2T(k,j,:) = p2(j,:)
                !p3T(k,j,:) = p3(j,:)
                p1q(k,j,:) = p1(j,:) - pq(k,j,:)
                p2q(k,j,:) = p2(j,:) - pq(k,j,:)
                p3q(k,j,:) = p3(j,:) - pq(k,j,:)
                ! get the cross product of p2q and p3q - u
                u(k,j,1) = p2q(k,j,2)*p3q(k,j,3) - p2q(k,j,3)*p3q(k,j,2)
                u(k,j,2) = p2q(k,j,3)*p3q(k,j,1) - p2q(k,j,1)*p3q(k,j,3)
                u(k,j,3) = p2q(k,j,1)*p3q(k,j,2) - p2q(k,j,2)*p3q(k,j,1)
                ! get the cross product of p3q and p1q - v
                v(k,j,1) = p3q(k,j,2)*p1q(k,j,3) - p3q(k,j,3)*p1q(k,j,2)
                v(k,j,2) = p3q(k,j,3)*p1q(k,j,1) - p3q(k,j,1)*p1q(k,j,3)
                v(k,j,3) = p3q(k,j,1)*p1q(k,j,2) - p3q(k,j,2)*p1q(k,j,1)
                ! get the cross product of p1q and p2q - w
                w(k,j,1) = p1q(k,j,2)*p2q(k,j,3) - p1q(k,j,3)*p2q(k,j,2)
                w(k,j,2) = p1q(k,j,3)*p2q(k,j,1) - p1q(k,j,1)*p2q(k,j,3)
                w(k,j,3) = p1q(k,j,1)*p2q(k,j,2) - p1q(k,j,2)*p2q(k,j,1)
                ! get the dot product of u and v
                uv(k,j) = sum(u(k,j,:)*v(k,j,:))
                ! get the dot product of w and u
                wu(k,j) = sum(w(k,j,:)*u(k,j,:))
                ! if uv > 0 and wu > 0, then the point is obstructed
                if (uv(k,j) > 0.0 .and. wu(k,j) > 0.0) then
                    cond(k,j) = 1
                end if
                !dummy_dist(k,j) = t(k) - tq(k,j)
                if (tq(k,j)> 0.0 .and. t(k)>tq(k,j)) then
                    distance(k,j) = 1
                end if
                checkobs(k) = checkobs(k) + cond(k,j)*distance(k,j)
            end do
        end do

        deallocate(p1q,p2q,p3q,u,v,w,wu,uv,cond,distance,dummy_dist)
    end subroutine check_obstruction

    subroutine get_deposition(num_sources,rank,s,sn,d,t,t_n,orientation,checkobs,thickness)
        real, dimension(:), intent(in) :: s,sn,t
        real, dimension(:,:), intent(in) :: d, t_n
        integer, dimension(:), intent(in) :: orientation, checkobs
        real, dimension(:), intent(out) :: thickness
        integer, intent(in) ::  rank, num_sources
        !real, dimension(:), allocatable :: dummy_phi, dummy_theta
        real, parameter :: PI_16 = 4 * atan (1.0_16)
        !real, allocatable, dimension(:) :: phi, theta
        real :: b,c
        integer :: n_t, k
        real :: a = 1.0E6
        !print*, "rank = ", rank, "source - s = ", s, "sn = ", sn
        n_t = size(t_n,1)
        !allocate(phi(n_t),theta(n_t))
        !allocate(dummy_phi(n_t),dummy_theta(n_t))
        !dummy_phi = (norm2(d,dim=2))*norm2(sn)
        !phi = sum(d*spread(sn,1,n_t),dim=2)/dummy_phi
        !dummy_theta = (norm2(d,dim=1)*norm2(t_n,dim=2))
        !theta = sum(-d*t_n,dim=2)/dummy_theta
        !print*, "d(1,9,:) = ", d(9,:), "t(1,9) = ", t(9)
        !print*, "building thickness for targets, n_t = ", n_t
        !print*, "check orientation and obstruction length = ", size(orientation), size(checkobs)
        do k = 1,n_t
            if (orientation(k) == 1 .and. checkobs(k) == 0) then
                b = sum(d(k,:)*sn)/(norm2(d(k,:))*norm2(sn))
                c = sum(-d(k,:)*t_n(k,:))/(norm2(d(k,:))*norm2(t_n(k,:)))
                thickness(k) = 1000*a*b*c/(0.534*PI_16*t(k)**2)
                !print *, "b = ", b, "d(k,3) = ", d(k,3), "k = ", k, "t(k) = ", t(k), "thickness(k) = ", thickness(k), &
                !"a = ", a, "c = ", c, "t_n(k,:) = ", t_n(k,:)
            else 
                thickness(k) = 0.0
                !print *, "k = ", k, "thickness(k) = ", thickness(k), "orientation(k) = ", orientation(k), & 
                !"checkobs(k) = ", checkobs(k)
            end if
        end do
        thickness = thickness/num_sources
    
        !print*, "rank = ", rank, "exiting get_deposition"
    end subroutine get_deposition

    subroutine check(ios, iomsg, action)
        integer, intent(in) :: ios
        character(len=*), intent(in) :: iomsg
        character(len=*), intent(in), optional :: action
        if (ios == 0) return  ! No error occured, return
        print*, "Error found. Error code:", ios
        print*, "Message: ", trim(iomsg)
        if (present(action)) print*, "Action was: ", trim(action)
        stop 1
    end subroutine check


end module mods

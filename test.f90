program test 
	real, dimension(:,:), allocatable :: a, b, s_x
    real, dimension(:), allocatable :: d

    allocate(a(5,3),b(5,3))
    allocate(s_x(1,3))
	! define a 
	a(1,:) = (/1.0, 0.0, 0.0/)
	a(2,:) = (/0.0, 2.0, 0.0/)
	a(3,:) = (/0.0, 0.0, 3.0/)
	a(4,:) = (/4.0, 4.0, 4.0/)
	a(5,:) = (/5.0, 5.0, 5.0/)

	! define b
	b(1,:) = (/5.0, 0.0, 0.0/)
	b(2,:) = (/0.0, 4.0, 0.0/)
	b(3,:) = (/0.0, 0.0, 3.0/)
	b(4,:) = (/2.0, 2.0, 2.0/)
	b(5,:) = (/1.0, 1.0, 1.0/)

    s_x(1,:) = (/1.0, 3.51, 2.876/)

    d = (/1.0, 2.0, 3.0, 4.0, 5.0/)

    !print*, "spread dim 1, 5 times", spread(s_x(1,:),1,5)
    print*, a*b
    !print*, a
    !print*, sum(a,dim=2) 
    print*, b
    print*, b(:,1)/d
    !print*, NORM2(b,dim=2)
	! write all to a file 
	print *, cos(90.0)
	open(17, file='burraah', status='unknown', action='write')
	do i=1,5
		write(17,*) a(i,1), a(i,2), a(i,3)
	end do
	close(17)

	
end program test
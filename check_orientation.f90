module check_orientation
	implicit none
	private
	public :: check_orientation

contains
	
	subroutine check_orientation(t_n, t_c, s_n, s_c, orientation)
		real, dimension(:), intent(in) :: t_n, t_c, s_n, s_c
		logical, dimension(:), intent(out) :: orientation
		real, dimension(size(t_n)) :: ts, st
		integer :: i
		real :: temp

		ts = sum(spread(s_n,1,size(t_n))-t_c)*t_n,dim=2)
		st = sum(t_c-spread(s_c,1,size(t_n)))*s_n,dim=2)
		orientation = ts*st > 0
	end subroutine check_orientation

end module check_orientation

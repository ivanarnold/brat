C FILE: branch_sub.f
      SUBROUTINE csec(istart, ifinish, imeta, ntemps, CSEC_DATA)
      implicit none

      INTEGER, allocatable :: LAT1(:),ISAT1(:),POINTER(:),indx(:)
      REAL, allocatable  :: EMESH1(:),ENAT(:), OMEGAR(:),
     &                        MATA(:,:),br(:),ctemp(:)
      INTEGER :: i,j,k,l,n, ierr, NAST1, MXE1, NOMT1, NZED1, NELC1
      INTEGER :: istart, ifinish, imeta, ntemps
      REAL, dimension(4, ntemps) :: CSEC_DATA
Cf2py intent(in) istart, ifinish, imeta, ntemps
Cf2py intent(out) CSEC_DATA

      CSEC_DATA = 0
      open(10,file='omega',form='formatted',status='unknown')
      open(20,file='bratin',form='formatted',status='unknown')
      read(20,*)
      read(20,*)

      allocate(indx(istart:ifinish))
      allocate(br(istart:ifinish))
      allocate(ctemp(istart:ifinish))

      DO I=istart,ifinish
        read(20,*)indx(i),br(i)
      ENDDO

C This sections reads the first two lines of every
C OMEGA to find out exactly how many points are present
C and to allocate accordingly

      READ(10,*)NZED1,NELC1
      READ(10,*)NAST1,MXE1,NOMT1

      allocate(LAT1(NAST1))         !! stores the L,S or 2J+1 values
      allocate(ISAT1(NAST1))
      allocate(EMESH1(MXE1))        !! stores the energy mesh of size mxe1
      allocate(POINTER(MXE1))
      allocate(ENAT(nast1))    !! stores energy values for the nast1 levels
      allocate(OMEGAR((nast1*(nast1-1))/2))
      allocate(MATA((NAST1*(NAST1-1)) !! stores A-values for all the
     &         /2,mxe1),stat=ierr)     !! transitions
      if(ierr.ne.0)stop ' allocation fails for MATA'

      READ(10,*)(ISAT1(I),LAT1(I),I=1,NAST1)
      READ(10,*)(ENAT(I),I=1,NAST1)

C Circulating round the energies for omega file
380   FORMAT(1pe14.8,6(1pe11.3)/(14x,6(e11.3)))
      K=0
      DO L=1,MXE1
        K=K+1
        READ(10,380)EMESH1(K),(MATA(N,K),N=1,NOMT1)
      ENDDO

C Create an aray of energies in eV
      DO i=1,ntemps
        emesh1(i) = emesh1(i) - enat(imeta)
        CSEC_DATA(1,i) = emesh1(i) * 13.6058
      ENDDO
      close(10)

C Calculate the apparent cross section
      ctemp=0.0
      DO i=1,ntemps
       DO j=istart,ifinish
         ctemp(j) = MATA(j,i) * br(j) * 87.974 /
     &  (abs(float(LAT1(imeta))) *  emesh1(i))
       ENDDO
       CSEC_DATA(2,i) = sum(ctemp)
      ENDDO

C Calculate the direct cross section
      ctemp=0.0
      DO i=1,ntemps
       DO j=istart,istart
         ctemp(j) = MATA(j,i) * br(j) * 87.974 /
     &  (abs(float(LAT1(imeta))) *  emesh1(i))
       ENDDO
       CSEC_DATA(3,i) = sum(ctemp)
      ENDDO

C Calculate the direct cross section
      ctemp=0.0
      DO i=1,ntemps
       DO j=istart+1,ifinish
         ctemp(j) = MATA(j,i) * br(j) * 87.974 /
     &  (abs(float(LAT1(imeta))) *  emesh1(i))
       ENDDO
       CSEC_DATA(4,i) = sum(ctemp)
      ENDDO

      END


C END FILE: branch_sub.f

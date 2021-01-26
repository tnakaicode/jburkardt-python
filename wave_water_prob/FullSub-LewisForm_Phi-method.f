*     Phi-Method Solving Diffraction and Radiation Problems
*           for a fully submerged Lewis-Form Cylinder
*          Incident Wave Comes from x-Positive  <-- 
*
      parameter ( ND=200*2+1, Nadd0=5, NaddD=ND+Nadd0*2 )
      real     K,Kd
      complex  zcen(NaddD),zeta(ND),zetaM
      real     thd(ND)
      complex  Xd,Yd,Md
      complex  Phi0  (ND)
      real     Phi0C (ND),Phi0S (ND)
      complex  Phi0d (ND),PsiB
      real     Phi0dC(ND),Phi0dS(ND)
      complex  zRhsvec(ND)
      real     A(NaddD,NaddD),RhsVec(NaddD),ReRhs(NaddD)
      real     U(NaddD,NaddD),V(NaddD,NaddD),ES(NaddD,NaddD)
      real     W(NaddD),R(NaddD),S(NaddD),Z(NaddD)
      integer  iEigen(ND),nEigen
      complex  Hdp,Hdm,H0dm
      character yorn*1
      complex  FC,FS,FCfunc
      real     ASumC(ND),ASumS(ND),ACDiag(ND),ASDiag(ND)
      real     Vn1(ND),Vn2(ND),Vn3(ND)
      real     nx(ND), ny(ND), nth(ND)
      complex  X1,Y1,M1
      complex  X2,Y2,M2
      complex  X3,Y3,M3
      complex  PhiR1 (ND),PhiR2 (ND),PhiR3 (ND)
      real     C(NaddD,NaddD)
      complex  HR1p,HR1m,HR2p,HR2m,HR3p,HR3m
      character LCol*1
      common   /LCol/LCol
*
      LCol='y'
**    LCol='n'
      call lcolor(7,3)
      write(6,'(/a)') '** Diffraction Problem for '//
     *           'a Submerged Lewis-Form Cylinder  **'
      call lcolor(3,0)
      write(6,*) 'Enter submergency  d/a, a...radius of circle'
      write(6,*) '  1.1  1.25  1.5  2'
      call lcolor(2,0)
      write(6,*) 'Ex. d =  1.25  1.5'
      read(5,*) d
 10   continue
         call  lcolor(7,3)
         write(6,'(/a,i6)') 'Max N is',ND/2
         write(6,'(a)')
     *       'Enter N ( 16 24 32 40 80 160 max 200 )'//
     *       'for Dividing a Whole Body (must be 4*int) >>'
         call lcolor(2,0)
         write(6,*) 'Enter  ''*'' to END'
         write(6,*) 'Standard N is  80  160   *'
         read(5,*,err=20,end=20) N
         N=(N/4)*4
         N2=N*2
 30      continue
            call lcolor(7,3)
            write(6,*) '********************************************'
            write(6,*) 'Enter            B/(2*d),sig1(x>0),sig2(x<0)'
            write(6,*) ' UnSymmetrical Body ( 1.0,  0.8500, 0.7000 )'
            write(6,*) '  Do.               ( 1.0,  0.9500, 0.5000 )'
            write(6,*) ' Circular Cylinder  ( 1.0,  0.7854, 0.7854 )'
            write(6,*) ' Elliptic Cylinder  ( 0.5,  0.7854, 0.7854 )'
            write(6,*) '  Do.               ( 0.100,0.7854, 0.7854 )'
            write(6,*) '  Do.               ( 0.010,0.7854, 0.7854 )'
            write(6,*) '  Do.               ( 0.001,0.7854, 0.7854 )'
            write(6,*) ' S1 Type            ( 1.0,  0.9400, 0.9400 )'
            write(6,*) ' S2 Type            ( 1.0,  0.6050, 0.6050 )'
            write(6,*) ' 1-Cusp             ( 0.2222,0.5236,0.5236 )'
            write(6,*) '  Do.               ( 0.0689,0.5689,0.5689 )'
            write(6,*) ' 2-Cusps            ( 0.2500,1.3989,1.3989 )'
            call lcolor(2,0)
            write(6,*) 'Enter  ''*'' to next N'
            write(6,*) ' Circular Cylinder ( 1.0,0.7854,0.7854 )'
            write(6,*) ' UnSymmtric Body   ( 1.0,0.9500,0.5000 )  *'
            read(5,*,err=40,end=40)    H0,sig1,sig2
            call lcolor(7,5)
            write(6, '(a/3f10.4)')     'H0,sig1,sig2 :',H0,sig1,sig2
*                _______                         **
            call coordnt(N,thd,zeta,zcen,zetaM,d,H0,sig1,sig2)
*                ~~~~~~~                         **
            call lcolor(3,0)
            write(6,*) 'Enter y to print coordinates'
            write(6,*) '      blank to skip'
            read(5,'(a1)') yorn
            if(yorn.eq.'y') then
               call lcolor(7,5)
               call vprt100(N,thd,'Theta(i) in deg.')
               call lcolor(5,0)
               call CVPRT     (N+1,zeta,'zeta(j)')
               call CVPRT     (N,  zcen,'zcen(i)')
            endif
 50         continue
               call lcolor(7,3)
               write(6,*) 'Enter Ka ( 0.4 0.6 0.8 1.0 1.2 2.0 * ) >>'
               call lcolor(2,0)
               write(6,*) 'Ex. Ka = 1   * for NEXT body config.'
               read(5,*,err=60,end=60) K
               Kd=K*d
               call lcolor(7,5)
               write(6,'(a,f10.5)') '**  Ka = w**2/g*a = ',K
               write(6,'(a,f10.5)') '**  Kd = w**2/g*d = ',Kd
* coemat            ______                                           **
               call coemat(NaddD,N,A,ASumC,ASumS,zeta,zcen,zetaM,K)
*                   ~~~~~~                                           **
               call lcolor(3,0)
               write(6,*) 'Enter y to write Asum(i),ADiag(i)'
               read(5,'(a1)') yorn
               if(yorn.eq.'y') then
                  do i=1,N
                     ACDiag(i  )=A(i  ,i)  
                     ASDiag(i  )=A(i  ,i+N)
                     ACDiag(i+N)=A(i+N,i)  
                     ASDiag(i+N)=A(i+N,i+N)
                  enddo
                  call lcolor(2,0)
                  call VPRT(N,ASumC,'Sum of A(i,j),j=1,N')
                  call VPRT(N,ASumS,'Sum of A(N+i,j),j=1,N')
                  call lcolor(4,0)
                  call VPRT(N2,ACDiag,'Diag of AC(i,j);i=1,2N,j=  1, N')
                  call VPRT(N2,ASDiag,'Diag of AS(i,j);i=1,2N,j=N+1,2N')
               endif
*
               call lcolor(3,0)
               write(6,*) 'Enter y to write A(i,j)'
               read(5,'(a1)') yorn
               if(yorn.eq.'y') then
                  call lcolor(5,0)
                  call APRT(NaddD,N2,N2,A,'Coef.-Matrix A(i,j)') 
**                call TPause('ASum,ADiagC,S')
               endif
* RhsVec for diffraction
**                  _______                               **
               call Phi0Cal(N,K,zcen,Phi0,Phi0C,Phi0S)
**                  ~~~~~~~                               **
               zRhsVec(1)=zRhsVec(1)
               do i=1,N
                  RhsVec(i)  =Phi0C(i)
                  RhsVec(N+i)=Phi0S(i)
                  zRhsVec(i)=cmplx(Phi0C(i),Phi0S(i))
               enddo
               RhsVec(N2+1)=0
               RhsVec(N2+2)=0
               call lcolor(3,0)
               write(6,*) 'Enter y to write RhsVec'
               write(6,*) '      blank to skip'
               read(5,'(a1)') yorn
               if(yorn.eq.'y') then
                  call lcolor(4,0)
                  call vprt(N2,RhsVec,'RhsVec(j),j=1,2N')
               endif
* Solve for diffraction
               eps=0.003
**                  _____                     **
               call SOLVE(NaddD,N2,N2,A,U,V,W,
**                  ~~~~~                     **
     *                    RhsVec,R,Z,S,.false.,eps,
     *                    nEigen,iEigen,ES)
               do i=1,N
                  Phi0dC(i)=S(  i)
                  Phi0dS(i)=S(N+i)
                  Phi0d (i)=dcmplx(Phi0dC(i),Phi0dS(i))
               enddo
               call lcolor(4,0)
               call CVPRT(N,Phi0d,'Phi(i)=phi0(i)+phid(i)')
**             call Vprt(N2,s,'s(j),j=1,2N')
*
               call lcolor(3,0)
               write(6,*) 'Enter y to write Re-Cal-RhsVec'
               write(6,*) '      blank to skip'
               read(5,'(a1)') yorn
               if(yorn.eq.'y') then
                  do i=1,N2
                     ReRhs(i)=0
                     do j=1,N2
                        ReRhs(i)=ReRhs(i)+A(i,j)*S(j)
                     enddo
                  enddo
                  call lcolor(6,0)
                  call vprt(N2,ReRhs,'Re-Cal-RhsVec(i),i=1,2*N')
               endif
*
* To Solve for Radiations
*   Vn Calculation
               call VnCal(N,Vn1,Vn2,Vn3,nx,ny,nth,zcen,zeta,d)
*   Set RhsMat Cij  ______                            **
               call RhsMat(NaddD,N,Nadd,C,zeta,zcen,K)
**                  ~~~~~~                            **
*   RhsVec for Vn1
               do i=1,N2
                  RhsVec(i)=0
                  do j=1,N
                     RhsVec(i)=RhsVec(i)+C(i,j)*Vn1(j)
                  enddo
               enddo
               do i=1,N
                  zRhsVec(i)=cmplx(RhsVec(i),RhsVec(N+i))
               enddo
               if(Nadd.ge.1) then
                  do i=1,Nadd
                     RhsVec(N2     +i)=0
                     RhsVec(N2+Nadd+i)=0
                     do j=1,N
                        RhsVec(N2     +i)=RhsVec(N2     +i)
     *                            +C(N2     +i,j)*Vn1(j)
                        RhsVec(N2+Nadd+i)=RhsVec(N2+Nadd+i)
     *                            +C(N2+Nadd+i,j)*Vn1(j)
                     enddo
                  enddo
               endif
**                  ______                     **
               call SOLVE1(NaddD,N2,N2,U,V,W,
**                  ~~~~~~                     **
     *                     RhsVec,R,Z,S,.false.,eps,
     *                     nEigen,iEigen,ES)
               do i=1,N
                  PhiR1(i)=cmplx(S(i),S(N+i))
               enddo
*   RhsVec for Vn2 
               do i=1,N2
                  RhsVec(i)=0
                  do j=1,N
                     RhsVec(i)=RhsVec(i)+C(i,j)*Vn2(j)
                  enddo
               enddo
               do i=1,N
                  zRhsVec(i)=cmplx(RhsVec(i),RhsVec(N+i))
               enddo
               if(Nadd.ge.1) then
                  do i=1,Nadd
                     RhsVec(N2     +i)=0
                     RhsVec(N2+Nadd+i)=0
                     do j=1,N
                        RhsVec(N2     +i)=RhsVec(N2     +i)
     *                            +C(N2     +i,j)*Vn2(j)
                        RhsVec(N2+Nadd+i)=RhsVec(N2+Nadd+i)
     *                            +C(N2+Nadd+i,j)*Vn2(j)
                     enddo
                  enddo
               endif
**                  ______                     **
               call SOLVE1(NaddD,N2,N2,U,V,W,
**                  ~~~~~~                     **
     *                     RhsVec,R,Z,S,.false.,eps,
     *                     nEigen,iEigen,ES)
               do i=1,N
                  PhiR2(i)=cmplx(S(i),S(N+i))
               enddo
*   RhsVec for Vn3  
               do i=1,N2
                  RhsVec(i)=0
                  do j=1,N
                     RhsVec(i)=RhsVec(i)+C(i,j)*Vn3(j)
                  enddo
               enddo
               do i=1,N
                  zRhsVec(i)=cmplx(RhsVec(i),RhsVec(N+i))
               enddo
               if(Nadd.ge.1) then
                  do i=1,Nadd
                     RhsVec(N2     +i)=0
                     RhsVec(N2+Nadd+i)=0
                     do j=1,N
                        RhsVec(N2     +i)=RhsVec(N2     +i)
     *                            +C(N2     +i,j)*Vn3(j)
                        RhsVec(N2+Nadd+i)=RhsVec(N2+Nadd+i)
     *                            +C(N2+Nadd+i,j)*Vn3(j)
                     enddo
                  enddo
               endif
**                  ______                     **
               call SOLVE1(NaddD,N2,N2,U,V,W,
**                  ~~~~~~                     **
     *                     RhsVec,R,Z,S,.false.,eps,
     *                     nEigen,iEigen,ES)
               do i=1,N
                  PhiR3(i)=cmplx(S(i),S(N+i))
               enddo
*__________________________________________________________________________
*    Post Processing
*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
               call lcolor(8,7)
               write(6,*) '*** Diffraction and Radiation Problem ***'
               call lcolor(4,0)
               write(6,'(a)') '**     d/a        **'
               write(6,'(5x,f8.4,f8.1)')   d
               write(6,'(a)') '**     Ka     Kd  **'
               write(6,'(5x,2f8.4)')  K,     Kd
               write(6,'(a)') '**     N          **'
               write(6,'(5x,2i3)')    N
* Kochin Functions
**
               HB=1
               H0=HB
**
               call Kochin(N,K,zeta,H0,
     *                     Phi0d,    Hdp, Hdm,H0dm,
     *                     PhiR1,Vn1,HR1p,HR1m,
     *                     PhiR2,Vn2,HR2p,HR2m,
     *                     PhiR3,Vn3,HR3p,HR3m,
     *                     E11,E21,E31,E12,E22,E32,E13,E23,E33)
*
               call KochWrt(K, Hdp, Hdm,H0dm,
     *                        HR1p,HR1m,
     *                        HR2p,HR2m,
     *                        HR3p,HR3m)
* Added Mass and Damping Coefficients
               call lcolor(8,7)
               write(6,*) '***** Added mass and Damping Coefficient'//
     *                    ' / Energy *****'
               write(6,'(a4,3(10x,a1,i1,a2,i1,5x))') 
     *                'Mode',   ('X',i,'/E',i,i=1,3)
               call EXForce(N,zeta,H0,nx,ny,nth,phiR1,'AD',X1,Y1,M1)
               call lcolor(6,0)
               write(6,'(a3,6f10.4)')             ' 1 ',X1, Y1, M1
               write(6,'(a8,f15.4,2f20.4)') '(Energy)',E11,E21,E31
               call EXForce(N,zeta,H0,nx,ny,nth,phiR2,'AD',X2,Y2,M2)
               call lcolor(4,0)
               write(6,'(a3,6f10.4)')             ' 2 ',X2, Y2, M2
               write(6,'(a8,f15.4,2f20.4)') '(Energy)',E12,E22,E32
               call EXForce(N,zeta,H0,nx,ny,nth,phiR3,'AD',X3,Y3,M3)
               call lcolor(3,0)
               write(6,'(a3,6f10.4)')             ' 3 ',X3, Y3, M3
               write(6,'(a8,f15.4,2f20.4)') '(Energy)',E13,E23,E33
* Wave Exciting Forces
               call EXForce(N,zeta,H0,nx,ny,nth,phi0d,'Ex',Xd,Yd,Md)
               call EXFoWrt(H0,Xd,Yd,Md,HR1p,HR2p,Hr3p)
* PsiC,S for diffraction
               PsiC=0
               PsiS=0
               do i=1,N
                  FC=FCfunc(zcen(i),K,N,zeta,Phi0d,FS)
                  PsiC=PsiC+imag(FC)
                  PsiS=PsiS+imag(FS)
               enddo
               PsiBC=PsiC/N
               PsiBS=PsiS/N
               PsiB=cmplx(PsiBC,PsiBS)
               call lcolor(8,7)
               call lcolor(4,0)
               write(6,'(a,2f10.3)') ' PsiBC,S =',PsiB
               eps=0.01
               FC=FCfunc(cmplx(0+eps,-d),K,N,zeta,Phi0d,FS)
               write(6,'(a,4f10.4)') 'FC, Fs at off-center are',FC,FS
               FC=FCfunc(cmplx(0-eps,-d+eps),K,N,zeta,Phi0d,FS)
               write(6,'(a,4f10.4)') 'FC, Fs at off-center are',FC,FS
               goto 50
 60         continue
            goto 30
 40      continue
         goto 10
 20   continue
      end
************************************************************************
      Subroutine QsCal(n2,q,z,ds,Phi)
*
*     Numerical Derivation of Phi by Quadratic Expansion
*
      complex z(*)
      real    Phi(*),q(*),ds(*)
*
      do j=1,n2-1
         ds(j)=abs(z(j+1)-z(j))
      enddo
      call dydx(Phi(1),ds(1),Phi(2),ds(2),Phi(3),dy1,dy2,dy3)
      q(1)=dy1
      do j=2,n2-1
         call dydx(Phi(j-1),ds(j-1),Phi(j),ds(j),Phi(j+1),dy1,dy2,dy3)
         q(j)=dy2
      enddo
      call dydx(Phi(n2-2),ds(n2-2),Phi(n2-1),ds(n2-1),Phi(n2),
     *          dy1,dy2,dy3)
      q(n2)=dy3
      end
******************************************************************************
      subroutine dydx(y1,ds1,y2,ds2,y3,dy1,dy2,dy3)
*
*      y1 ...  y2 ...  y3
*         ds1     ds2
*     dy1 ... dy2 ... dy3   = dy/dx
*
      den=ds1*ds2*(ds1+ds2)
      dy1=(2*ds1*ds2*(-y1+y2)+ds2**2*(-y1+y2)+ds1**2*(y2-y3))/den
      dy2=(ds2**2*(-y1+y2)+ds1**2*(-y2+y3))/den
      dy3=(ds2**2*(y1-y2)+ds1**2*(-y2+y3)+2*ds1*ds2*(-y2+y3))/den
      end
************************************************************************
      subroutine VnCal(N,Vn1,Vn2,Vn3,nx,ny,nth,z,zeta,d)
*
      real    Vn1(*),Vn2(*),Vn3(*)
      real    nx(*), ny(*), nth(*)
      complex z(*),zeta(*),dzeta
* 
**    HB=real(zeta(1))
      HB=1
      do j=1,N
         dzeta=zeta(j+1)-zeta(j)
         dj=abs(dzeta)
         dxsi=real(dzeta)
         deta=imag(dzeta)
* in IV-quadrant dxsi < 0, deta < 0 
*                  nx > 0,   ny > 0
*    Sign of Y and dy is reversed here to equal with ones defined by Kasiwagi 
         nx(j) =-deta/dj
         ny(j) =-dxsi/dj
         nth(j)=real(z(j))*ny(j)+(imag(z(j))+d)*nx(j)
         Vn1(j)= nx(j)
         Vn2(j)= ny(j)
         Vn3(j)= nth(j)/HB
         Vn1(N+j)=0
         Vn2(N+j)=0
         Vn3(N+j)=0
      enddo
      end
************************************************************************
      subroutine EXForce(N,zeta,HB,nx,ny,nth,phi,ADorEX,X,Y,M)
*
*  Pressure Integral
*     AD : Added Mass and Damping
*     EX : Wave Exciting Force
*
      complex zeta(*),phi(*),X,Y,M
      real    nx(*),ny(*),nth(*)
      character ADorEX*2
*
      X=0
      Y=0
      M=0
*  Wave Exciting Force for diffraction problem
      do j=1,N
         ds=abs(zeta(j+1)-zeta(j))/HB
         X=X+phi(j)*nx(j)*ds
         Y=Y+phi(j)*ny(j)*ds
         M=M+phi(j)*nth(j)/HB*ds
      enddo
*  Added Mass and Damping for radiation problem
      if(ADorEX.eq.'AD') then
         X=-conjg(X)/HB
         Y=-conjg(Y)/HB
         M=-conjg(M)/HB
      endif
      end
************************************************************************
      subroutine EXFoWrt(HB,X,Y,M,HR1p,HR2p,Hr3p)
*
      complex X,Y,M,HR1p,HR2p,Hr3p
      complex i/(0,1)/
      pi=acos(0.0)*2
      rd=180/pi
*
      aX=abs(X)
      aY=abs(Y)
      aM=abs(M)
      thX=real(-i*log(X/aX))*rd
      thY=real(-i*log(Y/aY))*rd
      thM=real(-i*log(M/aM))*rd
      call lcolor(8,7)
      write(6,*) '***** Wave Exciting Forces *****'
      write(6,*) 'Pressure Integral / Haskind-Newman ( Kochin Hi+ )'
      call lcolor(4,0)
      write(6,'(10x,3(6x,a),5x,a)') 'Real','Imag',' Abs',' Arg in deg.'
      call lcolor(6,0)
      write(6,'(a,3f10.4,f10.1)') '  Sway F. =',X,aX,thX
      write(6,'(a,3f10.4,f10.1)') '      H1+ =',HR1p/HB
      call lcolor(5,0)
      write(6,'(a,3f10.4,f10.1)') ' Heave F. =',Y,aY,thY
      write(6,'(a,3f10.4,f10.1)') '      H2+ =',HR2p/HB
      call lcolor(3,0)
      write(6,'(a,3f10.4,f10.1)') '  Roll M. =',M,aM,thM
      write(6,'(a,3f10.4,f10.1)') '      H3+ =',HR3p/HB
      end
************************************************************************
      subroutine Kochin(N,K,zeta,HB,
     *                   Phi0d,     Hdp, Hdm,H0dm,
     *                   PhiR1,Vn1,HR1p,HR1m,
     *                   PhiR2,Vn2,HR2p,HR2m,
     *                   PhiR3,Vn3,HR3p,HR3m,
     *                   E11,E21,E31,E12,E22,E32,E13,E23,E33)
*
      real    K,Vn1(*),Vn2(*),Vn3(*)
      complex zeta(*),dzeta
      complex Phi0d(*), Hdp, Hdm,H0dm
      complex PhiR1(*),HR1p,HR1m
      complex PhiR2(*),HR2p,HR2m
      complex PhiR3(*),HR3p,HR3m
      complex EiAlp,i/ (0.0,1.0) /
      complex EiKp2,EiKp1,EiKm2,EiKm1,dEiKm,dEiKp
**    complex dIp,dIm
*
      Hdp=0
      Hdm=0
      HR1p=0
      HR1m=0
      HR2p=0
      HR2m=0
      HR3p=0
      HR3m=0
      EiKp2=exp( i*K*conjg(zeta(1)))
      EiKm2=exp(-i*K   *   zeta(1))
      do j=1,N
         dzeta=zeta(j+1)-zeta(j)
         EiAlp=dzeta/abs(dzeta)
         EiKp1  =EiKp2
         EiKm1  =EiKm2
         EiKp2=exp( i*K*conjg(zeta(j+1)))
         EiKm2=exp(-i*K   *   zeta(j+1))
         dEiKp=EiKp2-EiKp1
         dEiKm=EiKm2-EiKm1
*
         Hdp =Hdp +i*dEiKp*Phi0d(j)
         Hdm =Hdm -i*dEiKm*Phi0d(j)
*
         HR1p=HR1p+i*dEiKp*(PhiR1(j)-Vn1(j)*Eialp/K)
         HR1m=HR1m-i*dEiKm*(PhiR1(j)-Vn1(j)/Eialp/K)
         HR2p=HR2p+i*dEiKp*(PhiR2(j)-Vn2(j)*Eialp/K)
         HR2m=HR2m-i*dEiKm*(PhiR2(j)-Vn2(j)/Eialp/K)
         HR3p=HR3p+i*dEiKp*(PhiR3(j)-Vn3(j)*Eialp/K)
         HR3m=HR3m-i*dEiKm*(PhiR3(j)-Vn3(j)/Eialp/K)
      enddo
      H0dm=-i+Hdm
* Energy
      HB2=HB**2
      E11=(HR1p*conjg(HR1p)+HR1m*conjg(HR1m))/2/HB2
      E21=(HR2p*conjg(HR1p)+HR2m*conjg(HR1m))/2/HB2
      E31=(HR3p*conjg(HR1p)+HR3m*conjg(HR1m))/2/HB2
      E12=(HR1p*conjg(HR2p)+HR1m*conjg(HR2m))/2/HB2
      E22=(HR2p*conjg(HR2p)+HR2m*conjg(HR2m))/2/HB2
      E32=(HR3p*conjg(HR2p)+HR3m*conjg(HR2m))/2/HB2
      E13=(HR1p*conjg(HR3p)+HR1m*conjg(HR3m))/2/HB2
      E23=(HR2p*conjg(HR3p)+HR2m*conjg(HR3m))/2/HB2
      E33=(HR3p*conjg(HR3p)+HR3m*conjg(HR3m))/2/HB2
      end
************************************************************************
      subroutine KochWrt(K, Hdp, Hdm,H0dm,
     *                     HR1p,HR1m,
     *                     HR2p,HR2m,
     *                     HR3p,HR3m)
*
      real K
      complex Hdp,Hdm,H0dm
      complex HR1p,HR1m,HR2p,HR2m,HR3p,HR3m
      complex i/(0,1)/,HdSym,HdAnt,HdpChk,HdmChk
      pi=acos(0.0)*2
      rd=180/pi
*
      AR1p=abs(HR1p)*K
      AR1m=abs(HR1m)*K
      AR2p=abs(HR2p)*K
      AR2m=abs(HR2m)*K
      AR3p=abs(HR3p)*K
      AR3m=abs(HR3m)*K
*
      Adm =abs(Hdm)
      Adp =abs(Hdp)
      A0dm=abs(H0dm)
*
      ER1p=atan2(-real(HR1p),imag(HR1p))*rd
      ER1m=atan2(-real(HR1m),imag(HR1m))*rd
      ER2p=atan2(-real(HR2p),imag(HR2p))*rd
      ER2m=atan2(-real(HR2m),imag(HR2m))*rd
      ER3p=atan2(-real(HR3p),imag(HR3p))*rd
      ER3m=atan2(-real(HR3m),imag(HR3m))*rd
*
      Edp =atan2(-real(Hdp), imag(Hdp))*rd
      Edm =atan2(-real(Hdm), imag(Hdm))*rd
      E0dm=atan2(-real(H0dm),imag(H0dm))*rd
      call lcolor(8,7)
      write(6,*) '***** Kochin Functions *****'
      call lcolor(6,0)
      write(6,'(20x,''** - **'',12x,''** + **'')')
      write(6,'( a,2f8.4,3x,2f8.4)')' H_Sway      =',HR1m,HR1p
      write(6,'(a,2(f8.4,f8.1,3x))')'    Amp,Eps  =',AR1m,ER1m,
     *                                               AR1p,ER1p
      call lcolor(5,0)
      write(6,'( a,2f8.4,3x,2f8.4)')' H_Heave     =',HR2m,HR2p
      write(6,'(a,2(f8.4,f8.1,3x))')'    Amp,Eps  =',AR2m,ER2m,
     *                                               AR2p,ER2p
      call lcolor(3,0)
      write(6,'( a,2f8.4,3x,2f8.4)')' H_Roll      =',HR3m,HR3p
      write(6,'(a,2(f8.4,f8.1,3x))')'    Amp,Eps  =',AR3m,ER3m,
     *                                               AR3p,ER3p
      call lcolor(2,0)
      write(6,'( a,2f8.4,3x,2f8.4)')' H_Diff      =', Hdm, Hdp
      write(6,'(a,2(f8.4,f8.1,3x))')'    Amp,Eps  =', Adm, Edm, Adp, Edp
      write(6,'( a,2f8.4)')         ' H0+H_Diff   =',H0dm
      write(6,'( a, f8.4,f8.1)')    '    Amp,Eps  =',A0dm,E0dm
*
      Eps1=ER1p/rd
      Eps2=ER2p/rd
      HdSym=i*exp(i*Eps2)*cos(Eps2)
      HdAnt=  exp(i*Eps1)*sin(Eps1)
      HdpChk=HdSym-HdAnt
      HdmChk=HdSym+HdAnt
      write(6,*) '( Computed from Radiation Solutions '//
     *           'for a Symmetric Body )'
      write(6,'( a,2f8.4,3x,2f8.4)')' H_Diff      =', HdmChk,HdpChk
*
      call lcolor(8,7)
      write(6,*) '***** Transmission and Reflection Coefficients *****' 
      call lcolor(2,0)
      H2=abs(H0dm)**2+abs(Hdp)**2
      write(6,'(a,2f10.4,f12.4)')' Ct, Cr, Eneg =',abs(H0dm),abs(Hdp),H2
      end
************************************************************************
      subroutine phi0Cal(N,K,zcen,phi0,phi0C,phi0S)
*
*    phi*0 = phi*0C + j * phi*0S
*
      real    K
      complex phi0(*),f0Cfunc,f0S
      real    phi0C(*),phi0S(*)
      complex zcen(*)

      do i=1,N
         phi0(i)= f0Cfunc(zcen(i),K,f0S)
         phi0C(i)=real(phi0(i))
         phi0S(i)=real(f0S)
      enddo
      end
************************************************************************
      complex function f0Cfunc(z,K,f0S)
*
*             f0*(z) = f0*C(z) + j * f0*S(z)
*     Complex function for incident wave comming from positive infty
*
      real    K
      complex z,f0S,i/(0,1)/
*
      f0Cfunc=exp(-i*K*z)
      f0S=i*f0Cfunc
      end
************************************************************************
      complex function v0Cfunc(z,K,v0S)
*
*             v0*(z) = v0*C(z) + j * v0*S(z)
*     Complex function for incident wave comming from positive infty
*
      real    K
      complex z,v0S,i/(0,1)/
*
      v0Cfunc=-i*K*exp(-i*K*z)
      v0S=i*v0Cfunc
      end
************************************************************************
      complex function fdCfunc(z,K,N,zeta,Phi0d,fdS)
*
*             fd*(z) = fd*C(z) + j * fd*S(z)     
*   Cuts are recognized as zeta(1), zeta(2), ..., zeta(N+1)
*        due to use of WGCfunc, LogNK and VLog
*
      real    K
      complex z,zeta(*),Phi0d(*)
      complex i/(0,1)/
      complex fdC,fdS
      complex WGCfunc,LogNK,VLog
      complex WGCj,WGCjp1,dWGCj
      complex WGSj,WGSjp1,dWGSj
*
      pi=acos(0d0)*2
      pi2=pi*2
      thetacut=pi/2
*
      fdC=0
      fdS=0
      WGCjp1=   WGCfunc(z,zeta(1),  K,thetacut,WGSjp1)
      do j=1,N
         WGCj =WGCjp1-i*LogNK(z,zeta(j),zeta(j+1))+i*VLog(z-zeta(j))
         WGSj =WGSjp1
         WGCjp1=WGCfunc(z,zeta(j+1),K,thetacut,WGSjp1)
         dWGCj=WGCjp1-WGCj
         dWGSj=WGSjp1-WGSj
         Phi0dCj=real(Phi0d(j))
         Phi0dSj=imag(Phi0d(j))
         fdC=fdC+Phi0dCj*dWGCj-Phi0dSj*dWGSj
         fdS=fdS+Phi0dCj*dWGSj+Phi0dSj*dWGCj
      enddo
      fdCfunc=fdC/pi2
      fdS    =fdS/pi2
      end
************************************************************************
      complex function vdCfunc(z,K,N,zeta,Phi0d,vdS)
*
*             vd*(z) = vd*C(z) + j * vd*S(z)     
*
      real    K
      complex z,zeta(*),Phi0d(*)
      complex vdC,vdS
      complex WmuCfunc
      complex WmuCj,WmuCjp1,dWmuCj
      complex WmuSj,WmuSjp1,dWmuSj
*
      pi=acos(0.0)*2
      pi2=pi*2
*
      vdC=0
      vdS=0
      WmuCjp1=   WmuCfunc(z,zeta(1),  K,WmuSjp1)
      do j=1,N
         WmuCj =WmuCjp1
         WmuSj =WmuSjp1
         WmuCjp1=WmuCfunc(z,zeta(j+1),K,WmuSjp1)
         dWmuCj=WmuCjp1-WmuCj
         dWmuSj=WmuSjp1-WmuSj
         Phi0dCj=real(Phi0d(j))
         Phi0dSj=imag(Phi0d(j))
         vdC=vdC+Phi0dCj*dWmuCj-Phi0dSj*dWmuSj
         vdS=vdS+Phi0dCj*dWmuSj+Phi0dSj*dWmuCj
      enddo
      vdCfunc=-vdC/pi2
      vdS    =-vdS/pi2
      end
************************************************************************
      complex function FCfunc(z,K,N,zeta,Phi0d,FS)
*
*             F(z) = FC(z)  + j * FS(z) = F*(z)/j
*                  = F*S(z) - j * F*C(z)
*

      real    K
      complex z,zeta(*),Phi0d(*)
      complex FS
      complex f0stC,f0stS,f0Cfunc
      complex fdstC,fdstS,fdCfunc
      complex FstC,FstS
*
      f0stC=f0Cfunc(z,K,f0stS)
      fdstC=fdCfunc(z,K,N,zeta,Phi0d,fdstS)
      FstC=f0stC+fdstC
      FstS=f0stS+fdstS
* Kasiwagi-values
      FCfunc= FstS
      FS    =-FstC
* star(*)-values
      FCfunc=FstC
      FS=FstS
      end
************************************************************************
      complex function VCfunc(z,K,N,zeta,Phi0d,VS)
*
*             V(z) = VC(z)  + j * VS(z) = V*(z)/j
*                  = V*S(z) - j * V*C(z)
*
      real    K
      complex z,zeta(*),Phi0d(*)
      complex VS
      complex v0stC,v0stS,v0Cfunc
      complex vdstC,vdstS,vdCfunc
      complex VstC,VstS
*
      v0stC=v0Cfunc(z,K,v0stS)
      vdstC=vdCfunc(z,K,N,zeta,Phi0d,vdstS)
      VstC=v0stC+vdstC
      VstS=v0stS+vdstS
* Kasiwagi-values
      VCfunc= VstS
      VS    =-VstC
* star(*)-values
      VCfunc=VstC
      VS=VstS
      end
************************************************************************
      function Eta0Cfunc(x,K,Eta0S)
*
*     Configuration for incident wave
*
      real    K
      complex z,f0Cfunc,f0stC,f0stS
*
      z=cmplx(x,0)
      f0stC=f0Cfunc(z,K,f0stS)
      Eta0Cfunc= real(-f0stC)
      Eta0S    =-real( f0stS)
      end
************************************************************************
      function EtadCfunc(x,K,N,zeta,Phi0d,EtadS)
*
*     Configuration for diffraction wave 
*
      real    K
      complex z,zeta(*),Phi0d(*)
      complex fdCfunc,fdstC,fdstS
*
      z=cmplx(x,0)
      fdstC=fdCfunc(z,K,N,zeta,Phi0d,fdstS)
      EtadCfunc= real(-fdstC)
      EtadS    =-real( fdstS)
      end
************************************************************************
      function EtaCfunc(x,K,N,zeta,Phi0d,EtaS)
*
*     Configuration for incident wave plus diffraction wave 
*
      real    K
      complex zeta(*),Phi0d(*)
*
      EtaCfunc=Eta0Cfunc(x,K,Eta0S)
     *        +EtadCfunc(x,K,N,zeta,Phi0d,EtadS)
      EtaS    =Eta0S+EtadS
      end
***********************************************************************
      subroutine coordnt(N,thd,zeta,zcen,zetaM,d,H0,sig1,sig2)
*
      complex zeta(*),zcen(*),zetaM
      real    thd(*)
*
      pi=acos(0d0)*2
      pi2=pi*2
      rd=180/pi
      dth=pi2/N
      epsth=dth*0.0006
* Lewis Form-1
      sigma=sig1
      rsub=(H0+1)**2+8*H0*(1-4*sigma/pi)
      amd =0.25*(3*(H0+1)-sqrt(rsub))
      a1  =0.5*(H0-1)/amd
      a3  =0.5*(H0+1)/amd-1
**    write(6,'(a,4f10.3)') 'H0,sigma,a1,a3 for 1 =',H0,sigma,a1,a3
*
      do i=1,N/2
         th=pi-dth*(i-1)
         if(i.eq.1) then
            th=th-epsth
         endif
         xi= amd*((1+a1)*sin(th)-a3*sin(3*th))
         yi=-amd*((1-a1)*cos(th)+a3*cos(3*th))
         zeta(i)=dcmplx(xi,yi-d)
      enddo
* Lewis Form-2
      sigma=sig2
      rsub=(H0+1)**2+8*H0*(1-4*sigma/pi)
      amd =0.25*(3*(H0+1)-sqrt(rsub))
      a1  =0.5*(H0-1)/amd
      a3  =0.5*(H0+1)/amd-1
**    write(6,'(a,4f10.3)') 'H0,sigma,a1,a3 for 2 =',H0,sigma,a1,a3
*
      do i=N/2+1,N+1
         th=pi-dth*(i-1)
         if(i.eq.N+1) then
            th=th+epsth
         endif
         xi= amd*((1+a1)*sin(th)-a3*sin(3*th))
         yi=-amd*((1-a1)*cos(th)+a3*cos(3*th))
         zeta(i)=dcmplx(xi,yi-d)
      enddo
* z-center and Theta
      do i=1,N
         zcen(i)=(zeta(i+1)+zeta(i))/2
         thd(i)=atan2(imag(zcen(i))+d,real(zcen(i)))*rd
         if(thd(i).gt.90) then
            thd(i)=thd(i)-360
         endif
      enddo
      zetaM=cmplx(0,-d)
      end
************************************************************************
      subroutine coemat(ND,N,A,ASumC,AsumS,zeta,zcen,zetaM,K)
*
      real    K
      real    A(ND,*),ASumC(*),ASumS(*)
      complex zeta(*),zcen(*),zetaM
      complex SGfunc
      complex SGij,SGijp1,dSij
*
      pi=acos(0d0)*2
      pi2=pi*2
*
      do i=1,N
         SGijp1=    SGfunc(zcen(i),zeta(1),K,zetaM)/pi2
         ASumC(i)=-real(SGijp1)
         ASumS(i)=-imag(SGijp1)
         do j=1,N
            SGij =SGijp1
            SGijp1 =SGfunc(zcen(i),zeta(j+1),K,zetaM)/pi2
            dSij=SGijp1-SGij
            if(i.ne.j) then
               A(  i,  j)=-real(dSij)
               A(N+i,  j)=-imag(dSij)
               A(  i,N+j)= imag(dSij)
               A(N+i,N+j)=-real(dSij)
            else
               A(  i,  j)=-real(dSij)+1
               A(N+i,  j)=-imag(dSij)
               A(  i,N+j)= imag(dSij)
               A(N+i,N+j)=-real(dSij)+1
            endif
            ASumC(i)=ASumC(i)+A(i,j)
            ASumS(i)=ASumS(i)+A(N+i,j)
         enddo
         ASumC(i)=ASumC(i)+real(SGijp1)
         ASumS(i)=ASumS(i)+imag(SGijp1)
      enddo
      end
************************************************************************
      subroutine RhsMat(ND,N,Nadd,C,zeta,zcen,K)
*
      real    K
      real    C(ND,*)
      complex zeta(*),zcen(*)
      complex WQintVCfunc,WQintC,WQintS
*
      pi=acos(0d0)*2
      pi2=pi*2
*
      do i=1,N
         do j=1,N
            WQintC=WQintVCfunc(zcen(i),zeta(j+1),zeta(j),K,WQintS)
            C(  i,  j)= real(WQintC)/pi2
            C(N+i,  j)= real(WQintS)/pi2
            C(  i,N+j)=-C(N+i,j)
            C(N+i,N+j)= C(i,j)
         enddo
      enddo
      N2=N*2
      do i=1,Nadd
         do j=1,N
           WQintC=WQintVCfunc(zcen(N+i),zeta(j+1),zeta(j),K,WQintS)
           C(N2     +i,  j)= real(WQintC)/pi2
           C(N2+Nadd+i,  j)= real(WQintS)/pi2
           C(N2     +i,N+j)=-C(N2+Nadd+i,j)
           C(N2+Nadd+i,N+j)= C(N2     +i,j)
         enddo
      enddo
      end
************************************************************************
      complex function SQfunc(z,zeta,K,ThetaCut)
*
      real    K
      complex z,zeta
      complex WQCfunc,WQC,WQS
*
      WQC=WQCfunc(z,zeta,K,ThetaCut,WQS)
      SQfunc=dcmplx(dble(WQC),dble(WQS))
      end
************************************************************************
      complex function TQfunc(z,zeta,K,ThetaCut)
*
      real    K
      complex z,zeta
      complex WQCfunc,WQC,WQS
*
      WQC=WQCfunc(z,zeta,K,ThetaCut,WQS)
      TQfunc=dcmplx(imag(WQC),imag(WQS))
      end
************************************************************************
      complex function SGfunc(z,zeta,K,zetaM)
*
*  z(j) is center between zeta(j+1) and zeta(j)
*       and recognized as existing outer region
*       due to use of WGNKCfunc
*
      real    K
      complex z,zeta,zetaM
      complex WGNKCfunc,WGC,WGS
*
      WGC=WGNKCfunc(z,zeta,K,zetaM,WGS)
      SGfunc=dcmplx(dble(WGC),dble(WGS))
      end
************************************************************************
      complex function TGfunc(z,zeta,K,ThetaCut)
*
      real    K
      complex z,zeta
      complex WGCfunc,WGC,WGS
*
      WGC=WGCfunc(z,zeta,K,ThetaCut,WGS)
      TGfunc=dcmplx(imag(WGC),imag(WGS))
      end
*****************************************************************       
      SUBROUTINE APRT(MD,M,N,A,TITLE)                                   
*                                                                       
*     ARRAY PRINT OUT in 10-colum type
*                                                                       
      REAL      A(MD,*) 
      CHARACTER TITLE*(*)                                               
*                                                                       
      J2=0                                                              
   10 CONTINUE                                                          
        IF(J2.NE.N) THEN                                                
        J1=J2+1                                                         
        J2=MIN(J1+9,N)                                                  
        I2=0                                                            
   20   CONTINUE                                                        
          IF(I2.NE.M) THEN                                              
          I1=I2+1                                                       
          I2=MIN(I1+49,M)                                               
          WRITE (6,100) TITLE                                           
          WRITE (6,110) (J,J=J1,J2)                                     
          DO 30 I=I1,I2                                                 
            WRITE (6,120) I,(A(I,J),J=J1,J2)                            
   30     CONTINUE                                                      
          GO TO 20                                                      
        ENDIF                                                           
        GOTO 10                                                         
      ENDIF                                                             
*                                                                       
  100 FORMAT(/5X,A)                                           
  110 FORMAT(8X,5(I3,4X),2X,5(I3,4X))                                 
  120 FORMAT(I4,2X,5F7.3,2X,5F7.3)                                      
      END                                                               
*****************************************************************       
      SUBROUTINE CAPRT(MD,M,N,A,TITLE)                    
*                                                                       
*     ARRAY PRINT OUT in 10-colum type
*                                                                       
      complex   A(MD,*) 
      CHARACTER TITLE*(*)                                               
*                                                                       
      J2=0                                                              
 10   IF(J2.NE.N) THEN                                                
         J1=J2+1                                                  
         J2=MIN(J1+4,N)                                           
         I2=0                                                     
 20      IF(I2.NE.M) THEN                                          
            I1=I2+1                                              
            I2=MIN(I1+49,M)                  
            WRITE (6,100) TITLE                                    
            WRITE (6,110) (J,J=J1,J2)                              
            DO 30 I=I1,I2                                        
               WRITE (6,120) I,(A(I,J),J=J1,J2)                   
 30         CONTINUE                                             
            GO TO 20                                              
         ENDIF                                    
         GOTO 10                                            
      ENDIF                             
  100 FORMAT(/10X,A)                                           
  110 FORMAT(6X,5(4x,I3,8X))
  120 FORMAT(I3,X,5(2F7.3,x))
      END                                                               
************************************************************************
      SUBROUTINE CVPRT(M,CV,TITLE)  
*                                   
*     COMPLEX-VECTOR PRINT OUT      
*                                   
      COMPLEX   CV(*)               
      INTEGER CLM(5) /1,2,3,4,5/    
      CHARACTER TITLE*(*)                                               
* 
      iW=6
      WRITE(iW,100) TITLE           
*                                   
      I2=0                          
      WRITE(iW,110) CLM             
*                                   
   20 CONTINUE                      
      IF (I2.EQ.M) RETURN           
      I0=I2                         
      I1=I2+1                       
      I2=I1+4                       
*                                   
      IF (I2.GT.M) I2=M             
      WRITE(iW,120) I0,(CV(I),I=I1,I2)
      GO TO 20                        
*                                     
  100 FORMAT (/5X,A)               
  110 FORMAT(I13,4I15)         
  120 FORMAT (1X,I3,5(1X,2F7.3)) 
      END                        
************************************************************************
      SUBROUTINE CVPRTiW(iW,M,CV,TITLE)  
*                                   
*     COMPLEX-VECTOR PRINT OUT      
*                                   
      COMPLEX   CV(*)               
      INTEGER CLM(5) /1,2,3,4,5/    
      CHARACTER TITLE*(*)                                               
* 
      WRITE(iW,100) TITLE           
*                                   
      I2=0                          
      WRITE(iW,110) CLM             
*                                   
   20 CONTINUE                      
      IF (I2.EQ.M) RETURN           
      I0=I2                         
      I1=I2+1                       
      I2=I1+4                       
*                                   
      IF (I2.GT.M) I2=M             
      WRITE(iW,120) I0,(CV(I),I=I1,I2)
      GO TO 20                        
*                                     
  100 FORMAT (/5X,A)               
  110 FORMAT(I13,4I15)         
  120 FORMAT (1X,I3,5(1X,2F7.3)) 
      END                        
*********************************************************************   
      SUBROUTINE VPRT(M,V,TITLE)                                        
*                                                                       
*     VECTOR PRINT OUT in 10-colum type
*                                                                       
      REAL      V(*)
      CHARACTER TITLE*(*)                                               
*                                                                       
      WRITE(6,100) TITLE                                                
      IMAX=MIN(10,M)                                                    
      WRITE (6,110) (I,I=1,IMAX)                                        
      I2=0                                                              
   10 CONTINUE                                                          
        IF (I2.NE.M) THEN                                               
        I1=I2+1                                                         
        I2=MIN(I1+9,M)                                                  
        WRITE (6,120) I1-1,(V(I),I=I1,I2)                               
        GO TO 10                                                        
      ENDIF                                                             
*                                                                       
  100 FORMAT (/10X,A)                                                 
  110 FORMAT(8X,5(I3,4X),2X,5(I3,4X))
  120 FORMAT(I4,2X,5F7.3,2X,5F7.3)                                      
      END                                                               
*********************************************************************   
      SUBROUTINE VPRT100(M,V,TITLE)                                        
*                                                                       
*     VECTOR PRINT OUT in 10-colum type
*                                                                       
      REAL      V(*)
      CHARACTER TITLE*(*)                                               
*                                                                       
      WRITE(6,100) TITLE                                                
      IMAX=MIN(10,M)                                                    
      WRITE (6,110) (I,I=1,IMAX)                                        
      I2=0                                                              
   10 CONTINUE                                                          
        IF (I2.NE.M) THEN                                               
        I1=I2+1                                                         
        I2=MIN(I1+9,M)                                                  
        WRITE (6,120) I1-1,(V(I),I=I1,I2)                               
        GO TO 10                                                        
      ENDIF                                                             
*                                                                       
  100 FORMAT (/5X,A)                                                 
  110 FORMAT(8X,5(I3,4X),2X,5(I3,4X),/)
  120 FORMAT(I4,2X,5F7.1,2X,5F7.1)                                      
      END                                                               
************************************************************************
      SUBROUTINE SOLVE(MD,MT,M1,A,U,V,W,G,R,Z,S,PFLG,EPS,
     *                 nEigen,iEigen,ES)
*                                                                       
*     TO SOLVE A*S=G BY USE OF SVD METHOD   A=A(MT*M1)                  
*         VERSION 0.1                                                   
*                                                                       
      DIMENSION A(MD,*),U(MD,*),V(MD,*),W(*),G(*),R(*),Z(*)      
      DIMENSION S(*),ES(MD,*)
      dimension iEigen(*)
      LOGICAL TRUE/.TRUE./                                              
      LOGICAL PFLG                                                      
*                                                                       
*     SVD METHOD                                                        
*                                                                       
      CALL SVD(MD,MT,M1,A,W,TRUE,U,TRUE,V,IERR,R)                       
*                                                                       
*     IERR,U,V,W, PRINT OUT                                             
*                                                                       
      IF(.NOT.PFLG) GO TO 10                                            
        WRITE(6,100)                                                    
        CALL APRT(MD,M1,M1,V,'V(I,J)  ')                                
   10 CONTINUE                                                          
*  
      call lcolor(8,2)
      WRITE(6,110) IERR                                                 
      if(IERR.ne.0) then
         write(6,'(i5,2f10.5,f16.5)') 
     *        IERR,W(IERR),R(IERR),R(IERR)/W(IERR)
         write(6,*) 'The other choise of N is recommended !'
         stop
      endif
**    CALL VPRT(M1,W,'W(I)    ')   
      Wmin1=W(1)
      Imin1=1
      Wmin2=W(1)
      Imin2=1
      DO I=2,M1   
         if(W(I).le.Wmin2) then
            Wmin2=W(I)
            Imin2=I
            if(Wmin2.le.Wmin1) then
               Wmindum=Wmin1
               Imindum=Imin1
               Wmin1=Wmin2
               Imin1=Imin2
               Wmin2=Wmindum
               Imin2=Imindum
            endif
         endif
**       write(6,'(i5,3f10.5,2i5)') I,W(I),Wmin1,Wmin2,Imin1,Imin2
      enddo
*                                                                       
*     ***  GIVE RHS, G, ONLY                                            
*                                                                       
      ENTRY SOLVE1    (MD,MT,M1,  U,V,W,G,R,Z,S,PFLG,EPS,
     *                 nEigen,iEigen,ES)
*                                                                       
*     TRANSPOSED(U)*G TO R                                              
*                                                                       
      DO 20 I=1,MT                                                      
        T=0                                                             
        DO 25 J=1,MT                                                    
          T=T+U(J,I)*G(J)                                               
   25   CONTINUE                                                        
        R(I)=T                                                          
   20 CONTINUE                                                          
**    CALL VPRT(M1,R,'R(I)    ')   
      call lcolor(2,0)
      write(6,'(/a)') '  Two Minimum Values of W(I)'
      write(6,'(a)') '         I     W(I)      R(I)          R(I)/W(I)'
      write(6,'(a,i5,2f10.5,f16.5)') 
     *        '  1st',Imin1,W(Imin1),R(Imin1),R(Imin1)/W(Imin1)
      write(6,'(a,i5,2f10.5,f16.5)') 
     *        '  2nd',Imin2,W(Imin2),R(Imin2),R(Imin2)/W(Imin2)
      write(6,'(a,f10.5,a)') 
     *        '          ',eps,'  is the given value for EPSIRON'
      call lcolor(0,0)
*                                                                       
*     SLUTION FOR  W*Z=R                                                
*     CHECK FOR EIGEN SOLUTION                                          
* 
      nEigen=0
      DO 40 I=1,M1   
         Z(I)=0.0                         
         IF(abs(W(I)).LE.EPS) GO TO 43               
         Z(I)=R(I)/W(I)                                                
      GO TO 40                                       
 43      CONTINUE   
         nEigen=nEigen+1
         iEigen(nEigen)=I
         DO 45 J=1,M1                           
            ES(J,nEigen)=V(J,I)                             
 45      CONTINUE                                 
         WRITE (6,120) I                                
**       CALL VPRT(M1,ES,'ES(I)   ')  
 40   CONTINUE                                                          
*                                                                       
*     SOLUTION FOR V*S=Z                                                
*                                                                       
      DO 50 I=1,M1                                                      
        T=0.0                                                           
        DO 55 J=1,M1                                                    
          T=T+V(I,J)*Z(J)                                               
   55   CONTINUE                                                        
        S(I)=T                                                          
   50 CONTINUE                                                          
*                                                                       
**    CALL VPRT(M1,S,'S(I)    ')                                        
      RETURN                                                            
  100 FORMAT('1')                                                       
  110 FORMAT(///5X,'IERR =',I4)                                         
  120 FORMAT('*****',I5,'-th  is  an Eigen Vector')     
      END                                                               
*****************************************************                   
      SUBROUTINE SVD(NM,M,N,A,W,MATU,U,MATV,V,IERR,RV1)                 
*                                                                       
      INTEGER I,J,K,L,M,N,II,I1,KK,K1,LL,L1,MN,NM,ITS,IERR              
      REAL  A(NM,N),W(N),U(NM,N),V(NM,N),RV1(N)                  
      REAL  C,F,G,H,S,X,Y,Z,SCALE,ANORM                        
      LOGICAL MATU,MATV                                                 
*                                                                       
      IERR=0                                                            
*                                                                       
      DO 100 I=1,M                                                      
*                                                                       
      DO 100 J=1,N                                                      
          U(I,J)=A(I,J)                                                 
  100 CONTINUE                                                          
*      HOUSEHOLDER REDUCTION TO BIDIAGONAL FORM                         
      G=0d0                                                             
      SCALE=0d0                                                         
      ANORM=0d0                                                         
*                                                                       
      DO 300 I=1,N                                                      
        L=I+1                                                           
        RV1(I)=SCALE*G                                                  
        G=0d0                                                           
        S=0d0                                                           
        SCALE=0d0                                                       
        IF(I.GT.M) GO TO 210                                            
*                                                                       
        DO 120 K=I,M                                                    
  120   SCALE=SCALE+ABS(U(K,I))                                         
*                                                                       
        IF(SCALE.EQ.0d0) GO TO 210                                      
*                                                                       
        DO 130 K=I,M                                                    
          U(K,I)=U(K,I)/SCALE                                           
          S=S+U(K,I)**2                                                 
  130   CONTINUE                                                        
*                                                                       
        F=U(I,I)                                                        
        G=-SIGN(SQRT(S),F)                                              
        H=F*G-S                                                         
        U(I,I)=F-G                                                      
        IF(I.EQ.N) GO TO 190                                            
*                                                                       
        DO 150 J=L,N                                                    
          S=0d0                                                         
*                                                                       
          DO 140 K=I,M                                                  
  140     S=S+U(K,I)*U(K,J)                                             
*                                                                       
          F=S/H                                                         
*                                                                       
          DO 150 K=I,M                                                  
            U(K,J)=U(K,J)+F*U(K,I)                                      
  150   CONTINUE                                                        
*                                                                       
  190   DO 200 K=I,M                                                    
  200   U(K,I)=SCALE*U(K,I)                                             
*                                                                       
  210   W(I)=SCALE*G                                                    
        G=0d0                                                           
        S=0d0                                                           
        SCALE=0d0                                                       
        IF(I.GT.M .OR. I.EQ.N) GO TO 290                                
*                                                                       
        DO 220 K=L,N                                                    
  220   SCALE=SCALE+ABS(U(I,K))                                         
*                                                                       
        IF(SCALE.EQ.0d0) GO TO 290                                      
*                                                                       
        DO 230 K=L,N                                                    
          U(I,K)=U(I,K)/SCALE                                           
          S=S+U(I,K)**2                                                 
  230   CONTINUE                                                        
*                                                                       
        F=U(I,L)                                                        
        G=-SIGN(SQRT(S),F)                                              
        H=F*G-S                                                         
        U(I,L)=F-G                                                      
*                                                                       
        DO 240 K=L,N                                                    
  240   RV1(K)=U(I,K)/H                                                 
*                                                                       
        IF(I.EQ.M) GO TO 270                                            
*                                                                       
        DO 260 J=L,M                                                    
          S=0d0                                                         
*                                                                       
          DO 250 K=L,N                                                  
  250     S=S+U(J,K)*U(I,K)                                             
*                                                                       
          DO 260 K=L,N                                                  
            U(J,K)=U(J,K)+S*RV1(K)                                      
  260   CONTINUE                                                        
*                                                                       
  270   DO 280 K=L,N                                                    
  280   U(I,K)=SCALE*U(I,K)                                             
*                                                                       
  290   ANORM=MAX(ANORM,ABS(W(I))+ABS(RV1(I)))                          
  300 CONTINUE                                                          
*      ACCUMULATION OF RIGHT-HAND TRANSFORMATIONS                       
      IF(.NOT.MATV) GO TO 410                                           
*      FOR I=N STEP -1 UNTIL 1 DO                                       
      DO 400 II=1,N                                                     
        I=N+1-II                                                        
        IF(I.EQ.N) GO TO 390                                            
        IF(G.EQ.0d0) GO TO 360                                          
*                                                                       
        DO 320 J=L,N                                                    
*      DOUBLE DIVISION AVOIDS POSSIBLE UNDERFLOW                        
  320   V(J,I)=(U(I,J)/U(I,L))/G                                        
*                                                                       
        DO 350 J=L,N                                                    
          S=0d0                                                         
*                                                                       
          DO 340 K=L,N                                                  
  340     S=S+U(I,K)*V(K,J)                                             
*                                                                       
          DO 350 K=L,N                                                  
            V(K,J)=V(K,J)+S*V(K,I)                                      
  350   CONTINUE                                                        
*                                                                       
  360   DO 380 J=L,N                                                    
          V(I,J)=0d0                                                    
          V(J,I)=0d0                                                    
  380   CONTINUE                                                        
*                                                                       
  390   V(I,I)=1d0                                                      
        G=RV1(I)                                                        
        L=I                                                             
  400 CONTINUE                                                          
*      ACCUMULATION OF LEFT-HAND TRANSFORMATIONS                        
  410 IF(.NOT.MATU) GO TO 510                                           
*      FOR I=MIN(M,N) STEP -1 UNTIL 1 DO                                
      MN=N                                                              
      IF(M.LT.N) MN=M                                                   
*                                                                       
      DO 500 II=1,MN                                                    
        I=MN+1-II                                                       
       L=I+1                                                            
        G=W(I)                                                          
        IF(I.EQ.N) GO TO 430                                            
*                                                                       
        DO 420 J=L,N                                                    
  420   U(I,J)=0d0                                                      
*                                                                       
  430   IF(G.EQ.0d0) GO TO 475                                          
        IF(I.EQ.MN) GO TO 460                                           
*                                                                       
        DO 450 J=L,N                                                    
          S=0d0                                                         
*                                                                       
          DO 440 K=L,M                                                  
  440     S=S+U(K,I)*U(K,J)                                             
*      DOUBLE DIVISION AVOIDS POSSIBLE UNDERFLOW                        
          F=(S/U(I,I))/G                                                
*                                                                       
          DO 450 K=I,M                                                  
            U(K,J)=U(K,J)+F*U(K,I)                                      
  450   CONTINUE                                                        
*                                                                       
  460   DO 470 J=I,M                                                    
  470   U(J,I)=U(J,I)/G                                                 
*                                                                       
        GO TO 490                                                       
*                                                                       
  475   DO 480 J=I,M                                                    
  480   U(J,I)=0d0                                                      
*                                                                       
  490   U(I,I)=U(I,I)+1d0                                               
  500 CONTINUE                                                          
*      DAIAGONALIZATION OF BIDIAGONAL FORM                              
*      FOR K=N STEP -1 UNTIL 1 DO                                       
  510 DO 700 KK=1,N                                                     
        K1=N-KK                                                         
        K=K1+1                                                          
        ITS=0                                                           
*      TEST FOR SPLITTING                                               
*        FOR L=K STEP -1 UNTIL 1 DO                                     
  520   DO 530 LL=1,K                                                   
          L1=K-LL                                                       
          L=L1+1                                                        
          IF(ABS(RV1(L))+ANORM.EQ.ANORM) GO TO 565                      
*      RV1(1) IS ALWAYS ZERO, SO THERE IS NO EXIT                       
*        THROUGH THE BOTTOM OF THE LOOP                                 
          IF(ABS(W(L1))+ANORM.EQ.ANORM) GO TO 540                       
  530   CONTINUE                                                        
*      CANCELLATION OF RV1(L) IF L GREATER THAN 1                       
  540   C=0d0                                                           
        S=1d0                                                           
*                                                                       
        DO 560 I=L,K                                                    
          F=S*RV1(I)                                                    
          RV1(I)=C*RV1(I)                                               
          IF(ABS(F)+ANORM.EQ.ANORM) GO TO 565                           
          G=W(I)                                                        
          H=SQRT(F*F+G*G)                                               
          W(I)=H                                                        
          C=G/H                                                         
          S=-F/H                                                        
          IF(.NOT.MATU) GO TO 560                                       
*                                                                       
          DO 550 J=1,M                                                  
            Y=U(J,L1)                                                   
            Z=U(J,I)                                                    
            U(J,L1)=Y*C+Z*S                                             
            U(J,I)=-Y*S+Z*C                                             
  550     CONTINUE                                                      
*                                                                       
  560   CONTINUE                                                        
*      TEST FOR CONVERGENCE                                             
  565   Z=W(K)                                                          
        IF(L.EQ.K) GO TO 650                                            
*      SHIFT FROM BOTTOM 2 BY 2 MINOR                                   
        IF(ITS.EQ.30) GO TO 1000                                        
        ITS=ITS+1                                                       
        X=W(L)                                                          
        Y=W(K1)                                                         
        G=RV1(K1)                                                       
        H=RV1(K)                                                        
        F=((Y-Z)*(Y+Z)+(G-H)*(G+H))/(2d0*H*Y)                           
        G=SQRT(F*F+1d0)                                                 
        F=((X-Z)*(X+Z)+H*(Y/(F+SIGN(G,F))-H))/X                         
*      NEXT QR TRANSFORMATION                                           
        C=1d0                                                           
        S=1d0                                                           
*                                                                       
        DO 600 I1=L,K1                                                  
          I=I1+1                                                        
          G=RV1(I)                                                      
          Y=W(I)                                                        
          H=S*G                                                         
          G=C*G                                                         
          Z=SQRT(F*F+H*H)                                               
          RV1(I1)=Z                                                     
          C=F/Z                                                         
          S=H/Z                                                         
          F=X*C+G*S                                                     
          G=-X*S+G*C                                                    
          H=Y*S                                                         
          Y=Y*C                                                         
          IF(.NOT.MATV) GO TO 575                                       
*                                                                       
          DO 570 J=1,N                                                  
            X=V(J,I1)                                                   
            Z=V(J,I)                                                    
            V(J,I1)=X*C+Z*S                                             
            V(J,I)=-X*S+Z*C                                             
  570     CONTINUE                                                      
*                                                                       
  575     Z=SQRT(F*F+H*H)                                               
          W(I1)=Z                                                       
*      ROTATION CAN BE ARBITRARY IF Z IS ZERO                           
          IF(Z.EQ.0d0) GO TO 580                                        
          C=F/Z                                                         
          S=H/Z                                                         
  580     F=C*G+S*Y                                                     
          X=-S*G+C*Y                                                    
          IF(.NOT.MATU) GO TO 600                                       
*                                                                       
          DO 590 J=1,M                                                  
            Y=U(J,I1)                                                   
            Z=U(J,I)                                                    
            U(J,I1)=Y*C+Z*S                                             
            U(J,I)=-Y*S+Z*C                                             
  590     CONTINUE                                                      
*                                                                       
  600   CONTINUE                                                        
*                                                                       
        RV1(L)=0d0                                                      
        RV1(K)=F                                                        
        W(K)=X                                                          
        GO TO 520                                                       
*      CONVERGENCE                                                      
  650   IF(Z.GE.0d0) GO TO 700                                          
*      W(K) IS MADE NON-NEGATIVE                                        
        W(K)=-Z                                                         
        IF(.NOT.MATV) GO TO 700                                         
*                                                                       
        DO 690 J=1,N                                                    
  690   V(J,K)=-V(J,K)                                                  
*                                                                       
  700 CONTINUE                                                          
*                                                                       
      GO TO 1001                                                        
*      SET ERROR - NO CONVERGENCE TO A                                  
*          SINGULAR VALUE AFTER 30 ITERATIONS                           
 1000 IERR=K                                                            
 1001 RETURN                                                            
      END                                                               
*******************************************************************************
      subroutine lcolor(fore,back)
*
*     0      1      2      3      4      5      6      7      8
*     stndrd black  red    green  blue   cyan   purple yellow white
* 
      integer   fore,back
      character cfore*3,cback*2
      character esc*2/'['/,eolm*1/'m'/,eol1m*3/';1m'/
      character LCol*1
      common   /LCol/LCol
*
      if(LCol.eq.'y') then
         if    (fore.eq.1) then
            cfore=';30'
         elseif(fore.eq.2) then
            cfore=';31'
         elseif(fore.eq.3) then
            cfore=';32'
         elseif(fore.eq.4) then
            cfore=';34'
         elseif(fore.eq.5) then
            cfore=';36'
         elseif(fore.eq.6) then
            cfore=';35'
         elseif(fore.eq.7) then
            cfore=';33'
         elseif(fore.eq.8) then
            cfore=';37'
         else
            cfore=';30'
         endif
         if(    back.eq.0) then
            cback='00'
         elseif(back.eq.1) then
            cback='40'
         elseif(back.eq.2) then
            cback='41'
         elseif(back.eq.3) then
            cback='42'
         elseif(back.eq.4) then
            cback='44'
         elseif(back.eq.5) then
            cback='46'
         elseif(back.eq.6) then
            cback='45'
         elseif(back.eq.7) then
            cback='43'
         elseif(back.eq.8) then
            cback='47'
         else
            cback='40'
         endif
         if( back.ne.0 ) then
            write(6,'(a)') esc//cback//cfore//eol1m
         else
            write(6,'(a)') esc//cback//cfore//eolm
         endif
      else
         write(6,*)
      endif
      end
************************************************************************
      complex function WQCfunc(z,zeta,K,ThetaCut,WQS)
*
*     Complex Potential of Wave Source WQ
*
*      ThetaCut ( Angle of Cut of Log(z-zeta) ) must be POSITIVE
*
*      ThetaCut - 2*pi  <    Argument of Log(z-zeta)      =<  ThetaCut
*                      .lt.                              .le.
*             - 3/2 PI  < Argument of Log(z-zetaBar) & E1 =<  PI/2
*
      real    K
      complex i/(0,1)/
      complex z,zeta,zetaBar,miKZ,E1
      complex LogZ,LogZBar,EmiKZ,SkappaC,SkappaS,WQS
      pi=acos(0.0)*2
      pi2=2*pi
      pih=pi/2
*
      LogZ=log(z-zeta)
      Alog=real(LogZ)
      ArgZ=imag(LogZ)
      if(ArgZ.le.ThetaCut-pi2) then
         ArgZ=ArgZ+pi2
      elseif(ArgZ.gt.ThetaCut) then
         ArgZ=ArgZ-pi2
      endif
      LogZ=cmplx(ALog,ArgZ)
*
      zetaBar=conjg(zeta)
      LogZBar=log(z-zetaBar)
      Alog=real(LogZBar)
      ArgZ=imag(LogZBar)
      if(ArgZ.gt.pih) ArgZ=ArgZ-pi2
      LogZBar=cmplx(ALog,ArgZ)
*
      miKZ=-i*K*(z-zetaBar)
      EmiKZ=exp(miKZ)
      call expint(miKZ,E1)
*
      xsign=real(z-zeta)
      if(xsign.gt.0) then
         SkappaC=EmiKZ*(E1-pi*i)
      else
         SkappaC=EmiKZ*(E1+pi*i)
      endif
      SkappaS=-pi*EmiKZ
      WQCfunc=LogZ-LogZBar-2*SkappaC
      WQS=-2*SkappaS
      end
***********************************************************************
      complex function WGCfunc(z,zeta,K,ThetaCut,WGS)
*
*     Complex Potential of Wave Vortex WG
*
*       ThetaCut ( Angle of Cut of Log(z-zeta) ) must be POSITIVE
*
*      ThetaCut - 2*pi  <    Argument of Log(z-zeta)      =<  ThetaCut
*                      .lt.                              .le.
*             - 3/2 PI  < Argument of Log(z-zetaBar) & E1 =<  PI/2
*
      real    K
      complex i/(0,1)/
      complex z,zeta,zetaBar,miKZ,E1
      complex LogZ,LogZBar,EmiKZ,SkappaC,SkappaS,WGS
*
      pi=acos(0.0)*2
      pi2=2*pi
      pih=pi/2
*
      LogZ=log(z-zeta)
      Alog=real(LogZ)
      ArgZ=imag(LogZ)
      if(ArgZ.le.ThetaCut-pi2) then
         ArgZ=ArgZ+pi2
      elseif(ArgZ.gt.ThetaCut) then
         ArgZ=ArgZ-pi2
      endif
      LogZ=cmplx(ALog,ArgZ)
*
      zetaBar=conjg(zeta)
      LogZBar=log(z-zetaBar)
      Alog=real(LogZBar)
      ArgZ=imag(LogZBar)
      if(ArgZ.gt.pih) ArgZ=ArgZ-pi2
      LogZBar=cmplx(ALog,ArgZ)
*
      miKZ=-i*K*(z-zetaBar)
      EmiKZ=exp(miKZ)
      call expint(miKZ,E1)
*
      xsign=real(z-zeta)
      if(xsign.gt.0) then
         SkappaC=EmiKZ*(E1-pi*i)
      else
         SkappaC=EmiKZ*(E1+pi*i)
      endif
      SkappaS=-pi*EmiKZ
      WGCfunc=-i*(LogZ+LogZBar)-2*i*SkappaC
      WGS=-2*i*SkappaS
      end
************************************************************************
      complex function WmuCfunc(z,zeta,K,WmuS)
*
*     Complex Potential of Wave -y-Doublet Wmu
*              = -d/dz(WG)
*
      real    K
      complex i/(0,1)/
      complex z,zeta,zetaBar,miKZ,E1
      complex InvZ,InvZBar,EmiKZ,SkappaC,SkappaS,WmuS
      pi=acos(0.0)*2
*
      InvZ=1/(z-zeta)
      zetaBar=conjg(zeta)
      InvZBar=1/(z-zetaBar)
      miKZ=-i*K*(z-zetaBar)
      EmiKZ=exp(miKZ)
      call expint(miKZ,E1)
      xsign=real(z-zeta)
      if(xsign.gt.0) then
         SkappaC=EmiKZ*(E1-pi*i)
      else
         SkappaC=EmiKZ*(E1+pi*i)
      endif
      SkappaS=-pi*EmiKZ
      WmuCfunc=i*InvZ-i*InvZBar+2*K*SkappaC
      WmuS=2*K*SkappaS
      end
************************************************************************
      complex function WQintVCfunc(z,zeta2,zeta1,K,WQintS)
*                      WQintV_C,S
*     
*     zeta1, zeta2 are exchangable
*
*     Cut of log(z-zeta) is set as
*        zeta1 -- zeta2 -- (xsi2,inf)
*
*     Cut of log(z-zetaBar) and E1 as
*        zetaBar -- (xsiBar,inf)
*
      real    K
      complex i/(0,1)/
      complex WQintC1,WQintC2
      complex WQintS1,WQintS2,WQintS
      complex z,zeta1,zeta2
      complex zdif,zdifBar,dzeta
      complex LogNK,VLog
      complex LogZ,LogZBar
      complex EiG,miKz,EmiKz,E1,SKappaC
      pi=acos(0.0)*2
      pi2=pi*2
*
      dzeta=zeta2-zeta1
      EiG=dzeta/abs(dzeta)
*
*     For zeta2
*
**    LogZ=LogNK(z,zeta2,zetaM)
**    LogZ=VLog(z-zeta2)
      zdif   =z-zeta2
      LogZ=VLog(zdif)
      zdifBar=z-conjg(zeta2)
      LogZBar=VLog(zdifBar)
      miKz=-i*K*zdifBar
      EmiKz=exp(miKz)
      call expint(miKZ,E1)
      if(real(z)-real(zeta2).gt.0) then
         SKappaC=EmiKz*(E1-pi*i)
      else
         SKappaC=EmiKz*(E1+pi*i)
      endif
      WQintC2=-conjg(EiG)*zdif   *(LogZ-1)
     *        +      EiG *zdifBar*(LogZBar-1)
     *        +i*2/K*EiG         *(LogZBar+SKappaC)
      WQintS2=-i*pi2/K*EiG*EmiKz
*
*     For zeta1
*
**    LogZ=LogNK(z,zeta1,zetaM)
      LogZ=LogNK(z,zeta1,zeta2)
      zdif=z-zeta1
*
      zdifBar=z-conjg(zeta1)
      LogZBar=VLog(zdifBar)
      miKz=-i*K*zdifBar
      EmiKz=exp(miKz)
      call expint(miKZ,E1)
      if(real(z)-real(zeta1).gt.0) then
         SKappaC=EmiKz*(E1-pi*i)
      else
         SKappaC=EmiKz*(E1+pi*i)
      endif
      WQintC1=-conjg(EiG)*zdif   *(LogZ-1)
     *        +      EiG *zdifBar*(LogZBar-1)
     *        +i*2/K*EiG         *(LogZBar+SKappaC)
      WQintS1=-i*pi2/K*EiG*EmiKz
*
      WQintVCfunc=WQintC2-WQintC1
      WQintS     =WQintS2-WQintS1
      end
***********************************************************************
      complex function WGNKCfunc(z,zeta,K,zetaM,WGS)
*                        WB
*
*     Wave Vortex with cut of Log like in N-K problem
*
*     Cut of log(z-zeta) is set as
*        zeta -- zetaM -- (xsiM,inf)
*                                  
*     Cut of log(z-zetaBar) as
*        zetaBar -- (xsiBar,inf)
*
*     Cut of E1 as
*        zeatBar -- (xsiBar,inf)
*
*
      real    K
      complex i/(0,1)/
      complex z,zeta,zetaM,zetaBar,miKZ,E1,LogNK
      complex LogZ,LogZBar,EmiKZ,SkappaC,SkappaS,WGS
*
      pi=acos(0.0)*2
      pi2=2*pi
      pih=pi/2
*          _____
      LogZ=LogNK(z,zeta,zetaM)
*          ~~~~~
      zetaBar=conjg(zeta)
      LogZBar=log(z-zetaBar)
      Alog=real(LogZBar)
      ArgZ=imag(LogZBar)
      if(ArgZ.gt.pih) ArgZ=ArgZ-pi2
      LogZBar=cmplx(ALog,ArgZ)
*
      miKZ=-i*K*(z-zetaBar)
      EmiKZ=exp(miKZ)
      call expint(miKZ,E1)
*
      xsign=real(z-zeta)
      if(xsign.gt.0) then
         SkappaC=EmiKZ*(E1-pi*i)
      else
         SkappaC=EmiKZ*(E1+pi*i)
      endif
      SkappaS=-pi*EmiKZ
      WGNKCfunc=-i*(LogZ+LogZBar)-2*i*SkappaC
      WGS=-2*i*SkappaS
      end
***************************************************************************
      complex function VLog(z)
*
*     Complex Logarithmic Function for Img(z) > 0
*     Cut : z -- (x,inf)
*
      complex z,pi2i
*
      pi=acos(0.0)*2
      pi2i=cmplx(0,pi*2)
      pih=pi/2
*
      VLog=log(z)
      if(imag(VLog).gt.pih) VLog=VLog-pi2i
      end
***************************************************************************
      complex function LogNK(z,zeta,zetaM)
*
*     Complex Logarithmic Function for Neumann-Kelvin Problem
*     Cut : zeta -- zetaM -- (xsiM,inf)
*     ( See Section 3.3.4 )
*
      complex z,zeta,zetaM,LogZ
*
      pi=acos(0.0)*2
      pi2=2*pi
*
      LogZ=log(z-zeta)
      Alog=real(LogZ)
      ArgZ=imag(LogZ)
*
      x=real(z)
      y=imag(z)
      xsi=real(zeta)
      eta=imag(zeta)
      xsiM=real(zetaM)
      etaM=imag(zetaM)
* Case I
      if(xsi.ge.xsiM .and. eta.ge.etaM) then
         if(x.lt.xsiM .and. y.ge.eta) then
            ArgZ=ArgZ-pi2
         elseif(x.ge.xsiM .and. y.lt.eta .and. 
     *          (y-etaM)*(xsi-xsiM).ge.(eta-etaM)*(x-xsiM)) then
            ArgZ=ArgZ+pi2
         endif
* Case II
      elseif(xsi.lt.xsiM .and. eta.ge.etaM) then
         if(x.lt.xsiM .and.
     *  (y.ge.eta .or.(y-eta)*(xsiM-xsi).ge.(etaM-eta)*(x-xsi))) then
            ArgZ=ArgZ-pi2
         endif            
* Case III
      elseif(xsi.lt.xsiM .and. eta.lt.etaM) then
         if(x.lt.xsiM .and. y.ge.eta .and. 
     *  (y-eta)*(xsiM-xsi).ge.(etaM-eta)*(x-xsi)) then
            ArgZ=ArgZ-pi2
         endif            
* Case IV
      else
         if(y.ge.eta .and. 
     *  (x.lt.xsiM .or.(y-etaM)*(xsi-xsiM).lt.(eta-etaM)*(x-xsiM))) then
            ArgZ=ArgZ-pi2
         endif            
      endif
      LogNK=cmplx(ALog,ArgZ)
      end
************************************************************************
      SUBROUTINE    EXPINT(z,e1)
*
*     EXPONENTIAL INTEGRAL OF COMPLEX ARGUMENT
*     CODED BY KATSUO SUZUKI (BODAI)
*
      IMPLICIT  COMPLEX  (Z)
      REAL INF/9.99999999999999D09/
      COMPLEX  E1,E1GL,EXPE1,LOGZ
      REAL GAMMA/0.5772156649D00/
      REAL PAI/3.14159265359D0/
**    RETURN
*
**    ENTRY  EXPI1 (Z,E1)
**    ENTRY  EXPI2 (Z,E1GL)
**    ENTRY  EXPI3 (Z,EXPE1)
**    ENTRY  EXPI4 (Z,ZEXPE1)
**    ENTRY  EXPIAL (Z,E1,E1GL,EXPE1,ZEXPE1)
*
*          E1 =COMPLEX EXPONENTIAL INTEGRAL OF COMPLEX ARGUMENT Z
*        E1GL =E1 + GAMMA + LOG( Z )
*       EXPE1 = EXP( Z ) * E1
*      ZEXPE1 = Z * EXPE1
*
      R=ABS(Z)
      X=real(Z)
      Y=IMAG(Z)
      IF(R.EQ.0.0)   GO TO 10
      LOGZ=LOG(Z)
      IF(R.GT.25.0)  GO TO 40
      IF(R.GT.4.0.AND.X.GE.0.0)  GO TO 30
      IF(ABS(Y).GT.4.0)  GO TO 30
      GO  TO 20
*
*         R = 0
*
   10 CONTINUE
      E1=DCMPLX(INF,0.0)
      E1GL=(1.0,0.0)
      EXPE1=E1
      ZEXPE1=DCMPLX(GAMMA,0.0)
      WRITE(6,100)
  100 FORMAT('   *** (EXPINT)  Z=(0.0,0.0)  ***')
      RETURN
*
*         SERIES  EXPANSION
*
*              E1GL= - S (-Z)**N/(N*FACT(N))
*                     N=1
*
   20 CONTINUE
      I=1
      ZI=Z
      ZSUM=ZI
   21 I=I+1
      A=-DFLOAT(I-1)/DFLOAT(I*I)
      ZI=A*ZI*Z
      ZSUM=ZSUM+ZI
      RE=ABS(ZSUM)
      AD=ABS(ZI)*1.0E8
      IF(RE.LE.AD)  GO TO 21
      E1GL=ZSUM
      E1=E1GL-GAMMA-LOGZ
      EXPE1=EXP(Z)*E1
      ZEXPE1=Z*EXPE1
      RETURN
*
*         CONTINUED  FRACTION
*
*              EXPE1 = 1/Z+1/1+1/Z+2/1+2/Z+3/1+3/Z+
*
   30 CONTINUE
      I=11
      Z0=(0.0,0.0)
      ZI=Z0
   31 IF(I.EQ.1) GO TO 35
      I=I-1
      AI=DFLOAT(I)
      ZD=Z+ZI
      IF(ZD.NE.0.0) GO TO 32
      ZI=Z0
      GO TO 33
   32 ZI=AI/ZD
   33 CONTINUE
      ZD=1.0+ZI
      IF(ZD.NE.0.0) GO TO 34
      ZI=Z0
      GO TO 31
   34 CONTINUE
      ZI=AI/ZD
      GO TO 31
   35 CONTINUE
      EXPE1=1.0/(Z+ZI)
      E1=EXP(-Z)*EXPE1
      E1GL=E1+GAMMA+LOGZ
      ZEXPE1=Z*EXPE1
      RETURN
*
*         ASYMPTOTIC EXPANSION
*
*              ZEXPE1 = 1-1/Z+FACT(2)/Z**2-FACT(3)/Z**3+
*
   40 CONTINUE
      ZINV=1.0/Z
      I=0
      ZI=(1.0,0.0)
      ZSUM=ZI
   41 I=I+1
      AI=DFLOAT(I)
      ZI=-AI*ZINV*ZI
      ZSUM=ZSUM+ZI
      RE=ABS(ZSUM)
      AD=ABS(ZI)*1.0E8
      IF(RE.LE.AD)  GO TO 41
      IF(Y.EQ.0.0.AND.X.LT.0.0)  ZSUM=ZSUM-Z*EXP(Z)*DCMPLX(0.0,PAI)
      ZEXPE1=ZSUM
      EXPE1=ZEXPE1*ZINV
      IF(-X.GE.200.0) GO TO 42
      E1=EXP(-Z)*EXPE1
      E1GL=E1+GAMMA+LOGZ
      RETURN
   42 E1=INF*EXP(DCMPLX(0.0,-Y))*EXPE1
      E1GL=E1+GAMMA+LOGZ
      RETURN
      END

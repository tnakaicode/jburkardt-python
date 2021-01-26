*     Problem of 2-D Hydro-Foil Problem in a uniform flow
*            Wave Making Resistance and Lift
*                                                    
      external    uv2func
      parameter ( nd=100)
      parameter ( n2d=nd*2,n2p1d=n2d+1)
      complex     i/(0,1)/
      real        xsi(n2p1d),Phi(n2p1d)
      complex     z(n2p1d),zeta(n2p1d),zetaM(n2p1d),zetaE
      complex     cDcL,kH,eIGamma,eIzeta,CPotent
      real        A(n2p1d,n2p1d),RhsVec(n2p1d),Asum(n2p1d),Diag(n2p1d)
      real        q(n2p1d),q0(n2p1d),qE(n2p1d),Cp(n2p1d),q2(n2p1d)
      real        U(n2p1d,n2p1d),V(n2p1d,n2p1d)                  
      real        W(n2p1d),R(n2p1d),ZVec(n2p1d),ES(n2p1d,n2p1d)
      integer     iEigen(n2p1d)
      logical     pflg/.false./
      parameter ( EpsSol=1e-5 )
      character*8 wingnm
      character   yorn*1
      character   LCol*1
      common     /LCol/LCol
      common     /Cpot/cK,n,q,zeta,zetaM,zetaE
*
      LCol='y'
**    LCol='n'
*
      call lcolor(7,3)
      write(6,*) '************************************************'
      write(6,*) 'Enter Wing No in 4-Figuers of NACA ( 4412 0012 ) '
      read(5,*) NACA
      call Body(wingnm,NACA)
      call lcolor(7,3)
      write(6,*) '************************************************'
      write(6,*) 'Enter Alpha ( Angle of Attack) ( 8 0 4 5 10 15 )'
      read(5,*) alpha
 10   continue
         call lcolor(7,5)
         write(6,'(3a,f4.1,a)') 'Wing is ',wingnm,
     *                          ', alpha =',alpha,' deg.'
         call lcolor(7,3)
         write(6,*) '************************************************'
         write(6,'(a,i3)')
     *       'Enter N, Half Mesh Number on Target Wing, N =< ',nd 
         write(6,*) '( 40 5 10 20 50 100 )  *'
         write(6,*) 'Enter ''*'' to go out of the LOOP'
         read(5,*,err=20,end=20) n
         n2=n*2
         n2p1=n2+1
         call lcolor(7,3)
         write(6,*) 'Enter iCase'
         write(6,*) '       2 for Using Gamma = 0 Cond. (n2+1 x n2+1)'
         write(6,*) '       1 for Using Kutta Condition (n2+1 x n2+1)'
         write(6,*) '       0 for Eigen Kutta Condition (n2   x n2+1)'
         write(6,*) '      -1 for Least Square sol.     (n2   x n2+1)'
**       read(5,*,end=40,err=40) iCase
         iCase=1
         call lcolor(7,3)
         write(6,*) 'Enter KDivMod'
         write(6,*) ' 1 for fine meshes near L.E. only '
         write(6,*) ' 0 for fine meshes near both edges Case-2(0-Gamma)'
**       read(5,*,err=40,end=40) KDivMod
         KDivMod=1
         call lcolor(7,5)
         write(6,'(a,i3)') 'iCadse  =',iCase,'KDivMod =',KDivMod
         call WingCdn (alpha,xsi,n,z,zeta,zetaM,zetaE,KDivMod)
         call lcolor(7,3)
         write(6,*) '************************************************'
         write(6,*)
     *        'Enter h/C > 0, depth of L.E. by Cord ( 0.78 1.03 )' 
         write(6,*) ' 0.75  1.0  1.5  2.0   * >>'
         read(5,*,end=40,err=40) h
         call lcolor(7,5)
         write(6,'(a,f7.3)') ' h/c =',h
         do j=1,n2p1
            zeta(j)=zeta(j)-i*h
         enddo
         do j=1,n2
            z(j)=z(j)-i*h
            zetaM(j)=zetaM(j)-i*h
         enddo
         zetaE=zetaE-i*h
         call lcolor(3,0)
         write(6,*) 'Enter y to print co-ordinates of wing'
         write(6,*) '      RETURN to skip'
         read(5,'(a)') yorn
         if(yorn.eq.'y') then
            call lcolor(4,0)
            call CVPRT(n2p1,zeta, 'BndryPnt(zeta)')               
            call CVPRT(n2,  z,    'Cntl-Pnt(z)')               
**          call CVPRT(n2,  zetaM,'Cut-Pnt(zetaM)')               
            write(6,'(/a,4f10.6)') '   z(1,n2)   =',z(1),z(n2)
            write(6,'( a,4f10.6)') 'zeta(1,n2p1) =',zeta(1),zeta(n2p1)
            write(6,'( a,2f10.6)') '   zetaE     =',zetaE
         endif
 30      continue
            call lcolor(7,3)
            write(6,*) '*********************************************'
            write(6,*)'Enter Froude Number based on Cord  '
            write(6,*)' 0 100 -1 , else : Usual Wave Making Condition'
            write(6,*)' |   |  |_ In Infinite Region'
            write(6,*)' |   |_____ High Speed Limit (Inv. Mirror Image)'
            write(6,*)' |__________ Low Speed Limit (Mirror Image)'
            write(6,*)' 0.6  1.0  0.5  0.75  2.0  *  >>'
            read(5,*,end=40,err=40) FnC
            if(Fnc.lt.0) then
               cK=-1
            elseif(Fnc.eq.0) then
               cK=50
            elseif(Fnc.lt.100) then
               cK=1/FnC**2
            else
               cK=0
            endif
            call lcolor(5,4)
            write(6,'(a,2f10.3)') 'FnC,cK =',FnC,cK
*                ______
            call CoeMat(n2p1d,n2p1,A,RhsVec,cK,z,zeta,zetaM,zetaE,iCase)
*                ~~~~~~
**          call VPRT(n2p1,RhsVec, 'RhsVector(j)')               
**          call APRT(n2p1d,n2p1,n2p1,A,'Coefficient Matrix(i,j)')  
            Diag(1)=Diag(1)
            do ii=1,n2
               Asum(ii)=0
               do j=1,n2
                  Asum(ii)=Asum(ii)+A(ii,j)
               enddo
               Diag(ii)=A(ii,ii)
            enddo
**          call lcolor(7,6)
**          call VPRT(n2,Asum,'Summed A(i)')
**          call lcolor(7,4)
**          call VPRT(n2,Diag,'Diag=A(i,i)')
            if(iCase.eq.2 .or. iCase.eq.1) then
*              Case 1 for Using  Kutta  Condition (n2+1 x n2+1)'
*              Case 2 for Using 0-Gamma Condition (n2+1 x n2+1)'
               call SOLVE
     *         (n2p1d,n2p1,n2p1,A,U,V,W,RhsVec,R,ZVec,q,pflg,epssol,
     *          nEigen,iEigen,ES)
            else
*              Case  0 for Using Eigen Solution & Kutta (n2 x n2+1)'
*              Case -1 for Only Least Square Solution   (n2 x n2+1)'
               call SOLVE
     *            (n2p1d,n2,n2p1,A,U,V,W,RhsVec,R,ZVec,q0,pflg,epssol,
     *             nEigen,iEigen,ES)
               do j=1,n2p1
                  qE(j)=ES(j,nEigen)
               enddo
               call lcolor(7,4)
               call VPRT(n2p1,q0,'Least Square Solution')
               write(6,'(/a,i2)') 'Number of EigenSol. is',nEigen
               call vprt(n2p1,qE,'Eigen Solution')
               if(iCase.eq.0) then
                  coef=-(q0(1)+q0(n2))/(qE(1)+qE(n2))
                  write(6,'(/a,f10.3)') 'Coef. =',coef
                  do j=1,n2p1
                     qE(j)=coef*qE(j)
                     q(j)=q0(j)+qE(j)
                  enddo
               else
                  do j=1,n2p1
                     q(j)=q0(j)
                  enddo
               endif
            endif
            qmin= 9999999
            qmax=-9999999
            do j=1,n2
               if(q(j).ge.qmax) qmax=q(j)
               if(q(j).le.qmin) qmin=q(j)
            enddo
            call lcolor(7,4)
**          call VPRT(n2,xsi,'xsi-coodinates')
            call VPRT(n2,q,' q_s(j) : Solved velocities around Wing')
            write(6,'(/a,2f10.3)') '  qMax,Min =',qmax,qmin
            write(6,'( a,2f10.3)') '-CpMax,Min =',qmax**2-1,qmin**2-1
            do j=1,n2
               Phi(j)=CPotent(z(j),n,zeta,q,cK,zetaM,zetaE)
            enddo
            call lcolor(4,0)
            call VPRT(n2,Phi,
     *           'Phi(j) : Calculated Velocity Potentials on Wing')
* Gamma, Cp, Cl,Cm,xCp, cDcL
            dPhi=Phi(1)-Phi(n2)
            Gamma=0
            do j=1,n2
               Gamma=Gamma-q(j)*abs(zeta(J+1)-zeta(j))
               q2(j)=q(j)**2
               Cp(j)=1-q2(j)
            enddo
            call ArDyProp(n2,q,xsi,Cl,Cm,xCp)
            cDcL=0
            do j=1,n2
               cDcL=cDcL+i*Cp(j)*(zeta(j+1)-zeta(j))
            enddo
            PsiB=q(n2p1)
* Kochin function
            kH=0
            do j=1,n2
               eIGamma=(zeta(j+1)-zeta(j))/(abs(zeta(j+1)-zeta(j)))
               eIzeta=exp(i*cK*conjg(zeta(j+1)))-
     *                exp(i*cK*conjg(zeta(j)))
               kH=kH+2*i*q(j)*eIGamma*eIzeta
            enddo
            cW=0.5/cK*abs(kH)**2
* Momentum Theory in y-direction
            call lcolor(7,2)
            write(6,*) 'Wait a while, now caculating'
            abserr=1e-2
            relerr=0
            xiF= 2
            xiA=-5
            call quanc8(uv2func,xiA,xiF,
     *           abserr,relerr,SF,errest,nofun,flag)
            eIzeta=kH*exp(-i*cK*xiA)
            SxiA=real(eIzeta)*imag(eIzeta)/cK
            cY=SF+2*Gamma+SxiA
* Results
            call lcolor(7,6)
            write(6,'(/a,   2f15.3)') '  PsiB, 2*dPhi  =',PsiB,dPhi*2 
            call lcolor(6,0)
            write(6,*) 'Momentum theory in y-direction gives '
            write(6,*) 'following 3 terms, the summation of them is cY'
            call lcolor(7,6)
            write(6,'(a,15x,f15.3,2f10.3)')' 2Gamma,SF,SxiA =',
     *                                      Gamma*2,SF,SxiA
**          call lcolor(6,0)
**          write(6,*) 'Moment, C.G., Lift from pressure integration'
**          call lcolor(7,6)
**          write(6,'(a,3f10.3)')    '  Cm, xCp, Cl   =',Cm, xCp, Cl
            call lcolor(6,0)
            write(6,*) 'Drag and Lift coef. from pressure integration '
            call lcolor(7,6)
            write(6,'(a,   2f15.3)') '    cD,    cL   =',conjg(cDcL)
            call lcolor(6,0)
            write(6,*) 'Lift coef. by momentum thoery '//
     *                 'must be eqaul to cL'
            call lcolor(7,6)
            write(6,'(a,15x,f15.3)') '           cY   =',cY
            call lcolor(6,0)
            write(6,*) 'Wave resistance from Kotchin function '//
     *                 'must be eqaul to cD'
            call lcolor(7,6)
            write(6,'(a,   2f15.3)') '    cW          =',cW
            goto 10
 20      continue
         goto 30
 40   continue 
      call lcolor(0,0)
      end
************************************************************************
      real function uv2func(x)
*
      parameter ( nd=100)
      parameter ( n2d=nd*2,n2p1d=n2d+1)
      complex     zeta(n2p1d),zetaM(n2p1d),zetaE
      complex     CVelocity,zpos,CV
      real        q(n2p1d)
*
      common /Cpot/cK,n,q,zeta,zetaM,zetaE
*
      zpos=cmplx(x,0.0)
      CV=CVelocity(zpos,n,zeta,q,cK,zetaM,zetaE)
      u= real(CV)
      v=-imag(CV)
      uv2func=u**2-v**2
      end
************************************************************************
      Subroutine ArDyProp(n2,q,xsi,Cl,Cm,xCp)
*
*     Lift, Moment and Center of Lift from pressure distribution
*
      real    xsi(*),q(*)
*
      n=n2/2
      Cl=0
      Cm=0
      do i=1,n
         Cl=Cl-(1-q(i)**2)*(xsi(i+1)-xsi(i))
         Cm=Cm-(1-q(i)**2)*(xsi(i+1)-xsi(i))*(xsi(i+1)+xsi(i))/2
      enddo
      xCp=Cm/Cl
      do i=n+1,n2
         Cl=Cl+(1-q(i)**2)*(xsi(i)-xsi(i+1))
         Cm=Cm+(1-q(i)**2)*(xsi(i)-xsi(i+1))*(xsi(i+1)+xsi(i))/2
      enddo
      xCp=Cm/Cl
      end
************************************************************************
      Subroutine CoeMat(n2p1d,n2p1,A,RhsVec,cK,z,zeta,zetaM,zetaE,iCase)
*
      real    A(n2p1d,*),RhsVec(*)
      complex z(*),zeta(*),zetaM(*),zetaE
      complex WGint
      pi=acos(0.0)*2
      pi2inv=1/(2*pi)
*
      do i=1,n2p1d
         RhsVec(i)=0
         do j=1,n2p1d
            A(i,j)=0
         enddo
      enddo
      n2=n2p1-1
      do i=1,n2
         RhsVec(i)=-imag(z(i))
         do j=1,n2
            A(i,j)=pi2inv*imag(WGint(z(i),zeta(j+1),zeta(j),cK,
     *                               zetaM(j),zetaE))
**          write(6,'(2i3,5f10.3)') i,j,z(i),zeta(j+1),A(i,j)
         enddo
      enddo
      do i=1,n2
         A(i,n2p1)=1
      enddo
      if(iCase.eq.1.or.iCase.eq.0) then
         A(n2p1,1) =1
         A(n2p1,n2)=1
      else
         do j=1,n2
            A(n2p1,j)=-abs(zeta(j+1)-zeta(j))
         enddo
      endif
      end
************************************************************************
      Subroutine WingCdn (alpha,xsi,n,z,zeta,zetaM,zetaE,KDivMod)
*     
*     Co-Ordinate for a Wing Section (Clockwise)
*  
      real xsi(*)
      complex z(*),zeta(*),zetaM(*),zetaE
      complex Eialpha,i/(0,1)/
      pi=acos(0.0)*2
      rd=pi/180
*     
      np1=n+1
      n2=2*n
      n2p1=n2+1 
      if(KDivMod.eq.1) then
*        Fine Meshes near Leading Edge Only        
         dth=pi/n*0.5
         do j=1,np1                                                     
            th=dth*(n-j+1)
            xsi(j)=-1+cos(th)
            xsi(n2p1-j+1)=xsi(j)
         enddo
      else
*        Fine Meshes near Both Edges        
         dth=pi/n
         do j=1,np1                                                     
            th=-pi+dth*(j-1)
            xsi(j)=0.5*(cos(th)-1)
            xsi(n2p1-j+1)=xsi(j)
         enddo
      endif
      ralpha=alpha*rd
      Eialpha=exp(i*ralpha)
      do j=1,np1
         xs=xsi(j)
         call BodyY(-xs,etau,etal,etam)
**       write(6,'(i3,4f10.3)') j,xs,etau,etal,etam
         zeta(j)       =cmplx(xs,etau)*Eialpha
         zeta(n2p1-j+1)=cmplx(xs,etal)*Eialpha
      enddo
      do j=1,n2
         z(j)=(zeta(j)+zeta(j+1))/2
      enddo
**    coefM=0.1
      coefM=0.2
      do j=1,n
         zetaM(j)     =z(j)+(z(n2-j+1)-z(j))*coefM
      enddo
      do j=1,n
         zetaM(n2-j+1)=z(j)+(z(n2-j+1)-z(j))*(1-coefM)
      enddo
      zetaE=(zeta(1)+zeta(n2p1))/2
**    call VPRT(np1,xsi,'Xsi0')               
      end                                                               
************************************************************************
      Subroutine Body (wingnm,NACA4D)                                   
*                                                                       
*     Wing Section NACA-Four-Digid-Series                               
*     yu = Upper Surface Coordinate                                     
*     yl = Lower Surface Coordinate                                     
*     x=0(L.E.) to 1(T.E.)
*     
      character wingnm*(*)
*     
      nm=NACA4D/1000                                                    
      m1=NACA4D-nm*1000                                                 
      np=m1/100                                                         
      nt=m1-np*100                                                      
      n3=nt/10                                                          
      n4=nt-n3*10                                                       
      t=nt*0.01                                                         
      p=np*0.1                                                          
      em=nm*0.01                                                        
      wingnm='NACA'                                                     
     *       //char(48+nm)//char(48+np)//char(48+n3)//char(48+n4)
      return
******
      Entry BodyY(x,yu,yl,ym)
*
      yt=t/0.2*(.2969*sqrt(x)+(-.126+(-0.3516+(.2843-.1015*x)*x)*x)*x)
      if(x.ge.p) then
         ym=em/(1-p)**2*((1-2*p)+2*p*x-x**2)
      else
         ym=em/p**2*x*(2*p-x)
      endif
      yu=ym+yt
      yl=ym-yt
      end                                                               
************************************************************************
      complex function CPotent(z,n,zeta,q,K,zetaM,zetaE)
*
*     Complex Potential around Wing
*     
      real    K
      complex WGint
      complex z,zeta(*),zetaM(*),zetaE
      real q(*)
      pi=acos(0.0)*2
      pi2=pi*2
      pi2Inv=1/pi2
*
      CPotent=-z
      do j=1,n*2
         CPotent=CPotent
     *         -pi2Inv*q(j)*WGint(z,zeta(j+1),zeta(j),K,zetaM(j),zetaE)
      enddo
      end
************************************************************************
      complex function CVelocity(z,n,zeta,q,K,zetaM,zetaE)
*
*     Complex Velocity around Wing
*     
      real    K
      complex VGint
      complex z,zeta(*),zetaM(*),zetaE
      real q(*)
      pi=acos(0.0)*2
      pi2=pi*2
      pi2Inv=1/pi2
*
      CVelocity=0
      do j=1,n*2
         CVelocity=CVelocity
     *         -pi2Inv*q(j)*VGint(z,zeta(j+1),zeta(j),K,zetaM(j),zetaE)
      enddo
      end
************************************************************************
      complex function VGint(z,zeta2,zeta1,K,zetaM,zetaE)
*                      VGintHF
*          For a Flow aroud a Submerged Hydro-Foil
*     Integrated Wave Vortex Segment
*            with zeta1, zeta2 and zetaM located clockwisely
*     Cut of log(z-zeta) is set as
*        zeta1,2 -- zetaM -- zetaE(T.E.) -- (-inf,etaE)
*     Cut of log(z-zetaBar) as
*        zetaBar -- (-inf,etaBar)
*        Note : Use vlog if you want to change the Cut to
*            zetaBar -- (xsiBar,inf)
*     Cut of E1 as
*        zeatBar --(xsiBar,inf)
*
*    0 < K < 50  : Usual Wave Making Condition
*        K >= 50 : Limit Case of Low Speed ( Mirror Image Flow)
*        K =  0  : Limit Case of High Speed ( Inverse Mirror Image Flow)
*        K <  0  : Infinite Region Flow
*
      real    K
      
      complex i/(0,1)/
      complex VGint1,VGint2
      complex z,zeta1,zeta2,zetaM,zetaE
      complex dzeta,zetaBar,zdifBar
      complex LogZ,LogZBar,LogHF
      complex EiG,miKz,EmiKz,E1,SKappa
      pi=acos(0.0)*2
      pi2=pi*2
*
      x=real(z)
      xsi1=real(zeta1)
      xsi2=real(zeta2)
      dzeta=zeta2-zeta1
*
*     For zeta2
*
      LogZ=LogHF(z,zeta2,zetaM,zetaE)
*
      zetaBar=conjg(zeta2)
      zdifBar=z-zetaBar
      LogZBar=Log(zdifBar)
      EiG=dzeta/abs(dzeta)
      if(K.lt.0)  then
         VGint2=i*conjg(EiG)*LogZ
      elseif(K.eq.0)  then
         VGint2=i*conjg(EiG)*LogZ+i*EiG*LogZBar
      elseif(K.lt.50) then
         miKz=-i*K*zdifBar
         EmiKz=exp(miKz)
         call expint(miKZ,E1)
         if(x-xsi2.ge.0) then
            SKappa=EmiKz*E1
         else
            SKappa=EmiKz*E1+pi2*i*EmiKz
         endif
         VGint2=i*conjg(EiG)*LogZ-i*EiG*LogZBar
     *         -2*i*EiG*SKappa
      else
         VGint2=i*conjg(EiG)*LogZ-i*EiG*LogZBar
      endif
*
*     For zeta1
*
      LogZ=LogHF(z,zeta1,zetaM,zetaE)
*
      zetaBar=conjg(zeta1)
      zdifBar=z-zetaBar
      LogZBar=Log(zdifBar)
**    EiG=dzeta/abs(dzeta)
      if(K.lt.0)  then
         VGint1=i*conjg(EiG)*LogZ
      elseif(K.eq.0)  then
         VGint1=i*conjg(EiG)*LogZ+i*EiG*LogZBar
      elseif(K.lt.50) then
         miKz=-i*K*zdifBar
         EmiKz=exp(miKz)
         call expint(miKZ,E1)
         if(x-xsi1.gt.0) then
            SKappa=EmiKz*E1
         else
            SKappa=EmiKz*E1+pi2*i*EmiKz
         endif
         VGint1=i*conjg(EiG)*LogZ-i*EiG*LogZBar
     *         -2*i*EiG*SKappa
      else
         VGint1=i*conjg(EiG)*LogZ-i*EiG*LogZBar
      endif
      VGint=VGint2-VGint1
      end
*************************************************************************
      complex function WGint(z,zeta2,zeta1,K,zetaM,zetaE)
*                      WGintHF
*          For a Flow aroud a Submerged Hydro-Foil
*     Integrated Wave Vortex Segment
*            with zeta1, zeta2 and zetaM located clockwisely
*     Cut of log(z-zeta) is set as
*        zeta1,2 -- zetaM -- zetaE(T.E.) -- (-inf,etaE)
*     Cut of log(z-zetaBar) as
*        zetaBar -- (-inf,etaBar)
*        Note : Use vlog if you want to change the Cut to
*            zetaBar -- (xsiBar,inf)
*     Cut of E1 as
*        zeatBar --(xsiBar,inf)
*
*    0 < K < 50  : Usual Wave Making Condition
*        K >= 50 : Limit Case of Low Speed ( Mirror Image Flow)
*        K =  0  : Limit Case of High Speed ( Inverse Mirror Image Flow)
*        K <  0  : Infinite Region Flow
*
      real    K
      complex i/(0,1)/
      complex WGint1,WGint2,LogHF
      complex z,zeta1,zeta2,zetaM,zetaE
      complex dzeta,zetaBar,zdif,zdifBar
      complex LogZ,LogZBar
      complex EiG,miKz,EmiKz,E1,SKappa
      pi=acos(0.0)*2
      pi2=pi*2
*
      x=real(z)
      xsi1=real(zeta1)
      xsi2=real(zeta2)
      dzeta=zeta2-zeta1
*
*     For zeta2
*
      LogZ=LogHF(z,zeta2,zetaM,zetaE)
      zdif=z-zeta2
*
      zetaBar=conjg(zeta2)
      zdifBar=z-zetaBar
      LogZBar=log(zdifBar)
      EiG=dzeta/abs(dzeta)
      if(K.lt.0)  then
         WGint2=i*conjg(EiG)*zdif*(LogZ-1)
      elseif(K.eq.0)  then
         WGint2=i*conjg(EiG)*zdif*(LogZ-1)+i*EiG*zdifBar*(LogZBar-1)
      elseif(K.lt.50) then
         miKz=-i*K*zdifBar
         EmiKz=exp(miKz)
         call expint(miKZ,E1)
         if(x-xsi2.ge.0) then
            SKappa=EmiKz*E1
         else
            SKappa=EmiKz*E1+pi2*i*EmiKz
         endif
         WGint2=i*conjg(EiG)*zdif*(LogZ-1)-i*EiG*zdifBar*(LogZBar-1)
     *         +2/K*EiG*LogZBar+2/K*EiG*SKappa
      else
         WGint2=i*conjg(EiG)*zdif*(LogZ-1)-i*EiG*zdifBar*(LogZBar-1)
      endif
*
*     For zeta1
*
      LogZ=LogHF(z,zeta1,zetaM,zetaE)
      zdif=z-zeta1
*
      zetaBar=conjg(zeta1)
      zdifBar=z-zetaBar
      LogZBar=log(zdifBar)
**    EiG=dzeta/abs(dzeta)
      if(K.lt.0)  then
         WGint1=i*conjg(EiG)*zdif*(LogZ-1)
      elseif(K.eq.0)  then
         WGint1=i*conjg(EiG)*zdif*(LogZ-1)+i*EiG*zdifBar*(LogZBar-1)
      elseif(K.lt.50) then
         miKz=-i*K*zdifBar
         EmiKz=exp(miKz)
         call expint(miKZ,E1)
         if(x-xsi1.gt.0) then
            SKappa=EmiKz*E1
         else
            SKappa=EmiKz*E1+pi2*i*EmiKz
         endif
         WGint1=i*conjg(EiG)*zdif*(LogZ-1)-i*EiG*zdifBar*(LogZBar-1)
     *         +2/K*EiG*LogZBar+2/K*EiG*SKappa
      else
         WGint1=i*conjg(EiG)*zdif*(LogZ-1)-i*EiG*zdifBar*(LogZBar-1)
      endif
      WGint=WGint2-WGint1
      end
************************************************************************
      complex function LogHF(z,zeta,zetaM,zetaE)
*
*     Complex Logarithmic Function 
*
*     Cut of Log(z-zeta):
*          (-Inf,etaE) - zetaE - zetaM -zeta
*
*
      complex z,zeta,zetaE,zetaM,LogZ
* 
      pi=acos(0.0)*2
      pi2=2*pi
*
      LogZ=log(z-zeta)
      Alog=real(LogZ)
      ArgZ=imag(LogZ)
*
      y=imag(z)
      eta=imag(zeta)
      etaE=imag(zetaE)
      etaM=imag(zetaM)
*
      AlpE=imag(log(zetaE-zeta))
      AlpM=imag(log(zetaM-zeta))
      ArgEM=imag(log(zetaE-zetaM))
      ArgME=imag(log(zetaM-zetaE))
      ArgZE=imag(log(z-zetaE))
      ArgZM=imag(log(z-zetaM))
      if(AlpE.lt.0) then
* Case I
         if(AlpM.ge.AlpE+pi) then
* Case I-1
            if(y.lt.eta) then
               if(y.ge.etaE .and. ArgZM.lt.ArgEM) then
                  ArgZ=ArgZ+pi2
               endif
            else
               if(ArgZM.ge.ArgEM .and. ArgZM.lt.AlpM-pi) then
                  ArgZ=ArgZ-pi2
               endif
            endif
         elseif(AlpM.ge.0) then
* Case I-2
            if(y.ge.etaE) then
               if(y.lt.eta.and.ArgZ.lt.AlpE  .or.
     *            ArgZ.ge.AlpE.and.ArgZ.lt.AlpM.and.ArgZM.lt.ArgEM) then
                  ArgZ=ArgZ+pi2
               endif
            endif
         elseif(AlpM.ge.AlpE) then
* Case I-3
            if(y.ge.etaE.and.y.lt.eta.and.ArgZ.lt.AlpE  .or.
     *         ArgZ.lt.AlpM.and.ArgZ.ge.AlpE.and.ArgZE.ge.ArgME) then
               ArgZ=ArgZ+pi2
            endif
         elseif(ArgME.ge.AlpE+pi) then
* Case I-4
            if(y.lt.eta.and.y.ge.etaM.and.ArgZ.lt.AlpM  .or.
     *         y.lt.etaM.and.y.ge.etaE.and.ArgZE.ge.ArgME) then
                 ArgZ=ArgZ+pi2
            endif
         else
* Case I-5 Out of Rule
            if(y.ge.etaE.and.y.lt.eta.and.ArgZ.lt.AlpE) then
               ArgZ=ArgZ+pi2
            endif
         endif
      else
* Case II
         if(AlpM.lt.AlpE-pi) then
* Case II-1
            if(y.ge.eta) then
               if(y.lt.etaE .and. ArgZM.ge.ArgEM) then
                  ArgZ=ArgZ-pi2
               endif
            else
               if(ArgZM.lt.ArgEM .and. ArgZM.ge.AlpM+pi) then
                    ArgZ=ArgZ+pi2
               endif
            endif
         elseif(AlpM.lt.0) then
* Case II-2
            if(y.lt.etaE) then
               ArgZM=imag(log(z-zetaM))
               if(y.ge.eta.and.ArgZ.ge.AlpE  .or.
     *            ArgZ.le.AlpE.and.ArgZ.ge.AlpM.and.ArgZM.ge.ArgEM) then
                  ArgZ=ArgZ-pi2
               endif
            endif
         elseif(AlpM.lt.AlpE) then
* Case II-3
            if(y.lt.etaE.and.y.ge.eta.and.ArgZ.ge.AlpE  .or.
     *         ArgZ.ge.AlpM.and.ArgZ.lt.AlpE.and.ArgZE.lt.ArgME) then
               ArgZ=ArgZ-pi2
            endif
         elseif(ArgME.lt.AlpE-pi) then
* Case II-4
            if(y.ge.eta.and.y.lt.etaM.and.ArgZ.ge.AlpM  .or.
     *         y.ge.etaM.and.y.lt.etaE.and.ArgZE.lt.ArgME) then
               ArgZ=ArgZ-pi2
            endif
         else
* Case II-5 Out of Rule
            if(y.lt.etaE.and.y.ge.eta.and.ArgZ.ge.AlpE) then
               ArgZ=ArgZ-pi2
            endif
         endif
      endif
*
      LogHF=cmplx(ALog,ArgZ)
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
  100 FORMAT(/10X,A)                                           
  110 FORMAT(8X,5(I3,4X),2X,5(I3,4X))                                 
  120 FORMAT(I4,2X,5F7.3,2X,5F7.3)                                      
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
  100 FORMAT(/5X,A)                                                 
  110 FORMAT(8X,5(I3,4X),2X,5(I3,4X))
  120 FORMAT(I4,2X,5F7.3,2X,5F7.3)                                      
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
      WRITE(6,100) TITLE           
*                                   
      I2=0                          
      WRITE(6,110) CLM             
*                                   
   20 CONTINUE                      
      IF (I2.EQ.M) RETURN           
      I0=I2                         
      I1=I2+1                       
      I2=I1+4                       
*                                   
      IF (I2.GT.M) I2=M             
      WRITE(6,120) I0,(CV(I),I=I1,I2)
      GO TO 20                        
*                                     
  100 FORMAT(/5X,A)               
  110 FORMAT(I13,4I15)         
  120 FORMAT(1X,I3,5(1X,2F7.3)) 
      END                        
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
************************************************************************
      SUBROUTINE SOLVE(MD,MT,M1,A,U,V,W,G,R,Z,S,PFLG,EPS,
     *                 nEigen,iEigen,ES)
*                                                                       
*     TO SOLVE A*S=G BY USE OF SVD METHOD   A=A(MT*M1)
*     *****     V.1 with respect to Eigen solutions    *****                  
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
      IF(PFLG) then
**       CALL APRT(MD,M1,M1,V,'V(I,J)  ')                                
      endif
* 
      call lcolor(2,0)
      WRITE(6,110) IERR  
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
**    ENTRY SOLVE1 (G,S,EPS)                                            
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
      if(PFLG) then
         call lcolor(4,0)
         CALL VPRT(M1,W,'W(I)    ')   
         CALL VPRT(M1,R,'R(I)    ')   
      endif
      call lcolor(6,0)
      write(6,'(/a)') '  Two Minimum Values of W(I)'
      write(6,'(a)') '         I     W(I)      R(I)          R(I)/W(I)'
      write(6,'(a,i5,2f10.5,3x,g16.5)') 
     *        '  1st',Imin1,W(Imin1),R(Imin1),R(Imin1)/W(Imin1)
      write(6,'(a,i5,2f10.5,3x,g16.5)') 
     *        '  2nd',Imin2,W(Imin2),R(Imin2),R(Imin2)/W(Imin2)
      write(6,'(a,f10.5,a)') 
     *        '          ',eps,'  is the given value of EPSIRON'
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
         if(PFLG) then
            call lcolor(6,0)
            WRITE (6,120) I                                
            CALL VPRT(M1,ES,'ES(I)   ')  
         endif
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
      if(PFLG) then
         call lcolor(6,0)
         CALL VPRT(M1,S,'S(I)    ')  
      endif                                      
      call lcolor(0,0)
      RETURN                                                            
  110 FORMAT(///5X,'IERR =',I4)                                         
  120 FORMAT('*****',I5,'-th  is  an Eigen Vector')     
      END                                                               
*************************************************************************
      SUBROUTINE SVD(NM,M,N,A,W,MATU,U,MATV,V,IERR,RV1)                 
*                                                                       
      INTEGER I,J,K,L,M,N,II,I1,KK,K1,LL,L1,MN,NM,ITS,IERR              
      REAL A(NM,N),W(N),U(NM,N),V(NM,N),RV1(N)                          
      REAL C,F,G,H,S,X,Y,Z,SCALE,ANORM                                  
      LOGICAL MATU,MATV                                                 
*                                                                       
*     THIS SUBROUTINE DETERMINES SIGULAR VALUE DECOMPOSITION       
*                                                                       
      IERR=0                                                            
*                                                                       
      DO 100 I=1,M                                                      
*                                                                       
      DO 100 J=1,N                                                      
          U(I,J)=A(I,J)                                                 
  100 CONTINUE                                                          
*      HOUSEHOLDER REDUCTION TO BIDIAGONAL FORM                         
      G=0.0                                                             
      SCALE=0.0                                                         
      ANORM=0.0                                                         
*                                                                       
      DO 300 I=1,N                                                      
        L=I+1                                                           
        RV1(I)=SCALE*G                                                  
        G=0.0                                                           
        S=0.0                                                           
        SCALE=0.0                                                       
        IF(I.GT.M) GO TO 210                                            
*                                                                       
        DO 120 K=I,M                                                    
  120   SCALE=SCALE+ABS(U(K,I))                                         
*                                                                       
        IF(SCALE.EQ.0.0) GO TO 210                                      
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
          S=0.0                                                         
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
        G=0.0                                                           
        S=0.0                                                           
        SCALE=0.0                                                       
        IF(I.GT.M .OR. I.EQ.N) GO TO 290                                
*                                                                       
        DO 220 K=L,N                                                    
  220   SCALE=SCALE+ABS(U(I,K))                                         
*                                                                       
        IF(SCALE.EQ.0.0) GO TO 290                                      
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
          S=0.0                                                         
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
        IF(G.EQ.0.0) GO TO 360                                          
*                                                                       
        DO 320 J=L,N                                                    
*      DOUBLE DIVISION AVOIDS POSSIBLE UNDERFLOW                        
  320   V(J,I)=(U(I,J)/U(I,L))/G                                        
*                                                                       
        DO 350 J=L,N                                                    
          S=0.0                                                         
*                                                                       
          DO 340 K=L,N                                                  
  340     S=S+U(I,K)*V(K,J)                                             
*                                                                       
          DO 350 K=L,N                                                  
            V(K,J)=V(K,J)+S*V(K,I)                                      
  350   CONTINUE                                                        
*                                                                       
  360   DO 380 J=L,N                                                    
          V(I,J)=0.0                                                    
          V(J,I)=0.0                                                    
  380   CONTINUE                                                        
*                                                                       
  390   V(I,I)=1.0                                                      
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
  420   U(I,J)=0.0                                                      
*                                                                       
  430   IF(G.EQ.0.0) GO TO 475                                          
        IF(I.EQ.MN) GO TO 460                                           
*                                                                       
        DO 450 J=L,N                                                    
          S=0.0                                                         
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
  480   U(J,I)=0.0                                                      
*                                                                       
  490   U(I,I)=U(I,I)+1.0                                               
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
  540   C=0.0                                                           
        S=1.0                                                           
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
        F=((Y-Z)*(Y+Z)+(G-H)*(G+H))/(2.0*H*Y)                           
        G=SQRT(F*F+1.0)                                                 
        F=((X-Z)*(X+Z)+H*(Y/(F+SIGN(G,F))-H))/X                         
*      NEXT QR TRANSFORMATION                                           
        C=1.0                                                           
        S=1.0                                                           
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
          IF(Z.EQ.0.0) GO TO 580                                        
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
        RV1(L)=0.0                                                      
        RV1(K)=F                                                        
        W(K)=X                                                          
        GO TO 520                                                       
*      CONVERGENCE                                                      
  650   IF(Z.GE.0.0) GO TO 700                                          
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
*****************************************************************************
      subroutine quanc8(fun,a,b,abserr,relerr,result,errest,nofun,flag)
c
**    double precision fun, a, b, abserr, relerr, result, errest, flag
      integer nofun
c
c   estimate the integral of fun(x) from a to b
c
      real qright(31),f(16),x(16),fsave(8,30),xsave(8,30)
      integer levmin,levmax,levout,nomax,nofin,lev,nim,i,j
c
c   ***   stage 1 ***   general initialization
c   set constants.
c
      levmin = 1
      levmax = 30
      levout = 6
      nomax = 5000
      nofin = nomax - 8*(levmax-levout+2**(levout+1))
c
c   trouble when nofun reaches nofin
c
      w0 =   3956.0d0 / 14175.0d0
      w1 =  23552.0d0 / 14175.0d0
      w2 =  -3712.0d0 / 14175.0d0
      w3 =  41984.0d0 / 14175.0d0
      w4 = -18160.0d0 / 14175.0d0
c
c   initialize running sums to zero.
c
      flag = 0.0d0
      result = 0.0d0
      cor11  = 0.0d0
      errest = 0.0d0
      area   = 0.0d0
      nofun = 0
      if (a .eq. b) return
c
c   ***   stage 2 ***   initialization for first interval
c
      lev = 0
      nim = 1
      x0 = a
      x(16) = b
      qprev  = 0.0d0
      f0 = fun(x0)
      stone = (b - a) / 16.0d0
      x(8)  =  (x0  + x(16)) / 2.0d0
      x(4)  =  (x0  + x(8))  / 2.0d0
      x(12) =  (x(8)  + x(16)) / 2.0d0
      x(2)  =  (x0  + x(4))  / 2.0d0
      x(6)  =  (x(4)  + x(8))  / 2.0d0
      x(10) =  (x(8)  + x(12)) / 2.0d0
      x(14) =  (x(12) + x(16)) / 2.0d0
      do 25 j = 2, 16, 2
         f(j) = fun(x(j))
   25 continue
      nofun = 9
c
c   ***   stage 3 ***   central calculation
c   requires qprev,x0,x2,x4,...,x16,f0,f2,f4,...,f16.
c   calculates x1,x3,...x15, f1,f3,...f15,qleft,qright,qnow,qdiff,area.
c
   30 x(1) = (x0 + x(2)) / 2.0d0
      f(1) = fun(x(1))
      do 35 j = 3, 15, 2
         x(j) = (x(j-1) + x(j+1)) / 2.0d0
         f(j) = fun(x(j))
   35 continue
      nofun = nofun + 8
      step = (x(16) - x0) / 16.0d0
      qleft  =  (w0*(f0 + f(8))  + w1*(f(1)+f(7))  + w2*(f(2)+f(6))
     1  + w3*(f(3)+f(5))  +  w4*f(4)) * step
      qright(lev+1)=(w0*(f(8)+f(16))+w1*(f(9)+f(15))+w2*(f(10)+f(14))
     1  + w3*(f(11)+f(13)) + w4*f(12)) * step
      qnow = qleft + qright(lev+1)
      qdiff = qnow - qprev
      area = area + qdiff
c
c   ***   stage 4 *** interval convergence test
c
      esterr = abs(qdiff) / 1023.0d0
      tolerr = max1(abserr,relerr*abs(area)) * (step/stone)
      if (lev .lt. levmin) go to 50
      if (lev .ge. levmax) go to 62
      if (nofun .gt. nofin) go to 60
      if (esterr .le. tolerr) go to 70
c
c   ***   stage 5   ***   no convergence
c   locate next interval.
c
   50 nim = 2*nim
      lev = lev+1
c
c   store right hand elements for future use.
c
      do 52 i = 1, 8
         fsave(i,lev) = f(i+8)
         xsave(i,lev) = x(i+8)
   52 continue
c
c   assemble left hand elements for immediate use.
c
      qprev = qleft
      do 55 i = 1, 8
         j = -i
         f(2*j+18) = f(j+9)
         x(2*j+18) = x(j+9)
   55 continue
      go to 30
c
c   ***   stage 6   ***   trouble section
c   number of function values is about to exceed limit.
c
   60 nofin = 2*nofin
      levmax = levout
      flag = flag + (b - x0) / (b - a)
      go to 70
c
c   current level is levmax.
c
   62 flag = flag + 1.0d0
c
c   ***   stage 7   ***   interval converged
c   add contributions into running sums.
c
   70 result = result + qnow
      errest = errest + esterr
      cor11  = cor11  + qdiff / 1023.0d0
c
c   locate next interval.
c
   72 if (nim .eq. 2*(nim/2)) go to 75
      nim = nim/2
      lev = lev-1
      go to 72
   75 nim = nim + 1
      if (lev .le. 0) go to 80
c
c   assemble elements required for the next interval.
c
      qprev = qright(lev)
      x0 = x(16)
      f0 = f(16)
      do 78 i = 1, 8
         f(2*i) = fsave(i,lev)
         x(2*i) = xsave(i,lev)
   78 continue
      go to 30
c
c   ***   stage 8   ***   finalize and return
c
   80 result = result + cor11
c
c   make sure errest not less than roundoff level.
c
      if (errest .eq. 0.0d0) return
   82 temp = abs(result) + errest
      if (temp .ne. abs(result)) return
      errest = 2.0d0*errest
      go to 82
      end
*******************************************************************************
      subroutine lcolor(fore,back)
*
*     0      1      2      3      4      5      6      7      8
*     stndrd black  red    green  blue   cyan   purple yellow white
* 
      integer fore,back
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

*     Semi-Submerged Circlular Cylinder Problem 
*                by Phi-method
*                                                    
* Note : Wave number nu is stated as K in this program
*        FscI = Re{df/dz+iKf}  on inner free furface
*
      parameter ( nd=100,np1d=nd+1 )
      complex     z(np1d),zeta(np1d)
      complex     CPotentOn,CVelocity,CVel,CPot
      real        A(np1d,np1d),RhsVec(np1d),Asum(np1d),Diag(np1d)
      real        Phi(np1d)
      real        qcal(np1d),qcald(np1d),ds(np1d)
      real        Phical(np1d),Psical(np1d)
      real        LmbA,LmbI,LmbF
      real        U(np1d,np1d),V(np1d,np1d)                  
      real        W(np1d),R(np1d),ZVec(np1d),ES(np1d)
      logical     pflg/.false./
**    logical     pflg/.true./
      parameter ( EpsSol=1e-5 )
      character   cond*27,CASE*1,yorn*1,LCol*1
      common     /LCol/LCol
*
      LCol='y'
**    LCol='n'
 100  continue
      call lcolor(7,3)
         write(6,*) '**************************************************'
      write(6,'(a,i4)') 'Enter N, Mesh Number on the Body =< ',ND 
      write(6,'(a,i4)') ' 50  30  100  *'
      write(6,'(a,i4)') '     Enter ''*'' to go out of LOOP'
      read(5,*,err=110,end=110) n
      np1=n+1
      call BodyCdn(n,z,zeta)
      call lcolor(3,0)
      write(6,*) 'Enter y to print co-ordinates'
      write(6,*) '      RETURN to skip'
      read(5,'(a)') yorn
      if(yorn.eq.'y') then
         call lcolor(4,0)
         call CVPRT  (np1,zeta, 'BndryPnt(zeta), j=1,n+1')               
         call CVPRT  (n,  z,    'Cntl-Pnt(z), i=1,n')
      endif 
 10   continue
         call lcolor(7,3)
         write(6,*) '**************************************************'
         write(6,*) 'Enter Ka, Wave Number based on Radius  *'
         write(6,*) '            1e9  :  Low Speed Limit (Mirror Image)'
         write(6,*) '      K  =  0.2  0.4  0.6  0.8  1.0  2.0  4.0  *'
         read(5,*,end=20,err=20) cK
         call lcolor(5,4)
         write(6,'(/a,f10.3,i5,a)') '*** Ka, n =',cK,n,' ***'
         icount=0
 30      continue
            icount=icount+1
            call lcolor(6,0)
            write(6,'(a,f5.2,a)') 'Last Kappa & CASE = ',cK,'  '//CASE
            call lcolor(7,3)
            write(6,*) '**********************************************'
            write(6,*) 'Case LmbF PsiB LmbA   : Type of Solution'
            write(6,*) '  R     0  1/K    0   : Regular Sol.'
            write(6,*) '  Z     0    0    0   : Zero-Vertical Flux Sol.'
            write(6,*) '  F     0    0 -1/K   : +WQ at F.P.'
            write(6,*) '  A     0  1/K  1/K   : -WQ at A.P.'
            write(6,*) '  O     0  any  any   : Other Any Sol.'
            write(6,*) 'Enter CASE ( R Z F A O * ) >>'
            read(5,'(a)',err=40,end=40) CASE
            call lcolor(4,0)
         if(CASE.eq.'*') goto 40
            LmbI=-1/cK
            LmbF=0
            if    (CASE.eq.'R') then
               write(6,'(a)') '**** CASE : R ****'
               cond='           Regular Solution'
               PsiB=1/cK
               LmbA=0
               FSCI=0
               YKF=PsiB*cK
               YKA=1+(FSCI-LmbA)*cK
            elseif(CASE.eq.'Z') then
               write(6,'(a)') '**** CASE : Z ****'
               cond='Zero-Vertical Flux Solution'
               PsiB=0
               LmbA=0
               FSCI=-1/cK
               YKF=PsiB*cK
               YKA=1+(FSCI-LmbA)*cK
            elseif(CASE.eq.'F') then
               write(6,'(a)') '**** CASE : F ****'
               cond='        WQ at F.P. Solution'
               PsiB=0
               LmbA=-1/cK
               FSCI=LmbA
               YKF=PsiB*cK
               YKA=1+(FSCI-LmbA)*cK
             elseif(CASE.eq.'A') then
               write(6,'(a)') '**** CASE : A ****'
               cond='       -WQ at A.P. Solution'
               PsiB=1/cK
               LmbA=1/cK
               FSCI=0
               YKF=PsiB*cK
               YKA=1+(FSCI-LmbA)*cK
            else
               write(6,'(a)') '**** CASE : O ****'
               cond='             Other Solution'
               call lcolor(7,3)
               write(6,*) 'Enter Values of KyA, KyF'//
     *                    ' ( K*Eta at PA, PF )'
               write(6,*) 'Ex.  0.5   -0.5'
               read(5,*,end=40,err=40) YKA,YKF
               PsiB=YKF/cK
               LmbA=(YKF-YKA)/cK
               FSCI=(YKF-1)/cK
            endif
            call lcolor(7,4)
            write(6,'(2a,2f8.3)') '   '//cond,' K, 1/K =',cK,1/cK
*
            call RhsVecC(n,RhsVec,cK,PsiB,LmbA,LmbI,z,zeta)
            if(icount.eq.1) then
*                   ______
               call CoeMat(np1d,n,A,cK,z,zeta)
*                   ~~~~~~
               call lcolor(3,0)
               write(6,*) 'Enter y to print Sum of A(i,j) and A(i,i)'
               write(6,*) '      RETURN to skip'
               read(5,'(a)') yorn
               if(yorn.eq.'y') then
                  do ii=1,n
                     Asum(ii)=0
                     do j=1,n
                        Asum(ii)=Asum(ii)+a(ii,j)
                     enddo
                     Diag(ii)=a(ii,ii)
                  enddo
                  call lcolor(7,4)
                  call vprt(n,Asum,'Sum of A(i,j) for j=1,N')
                  call vprt(n,Diag,'Diag. Elem. A(i,i)')
               endif
**             call VPRT(n,RhsVec, 'RhsVector(j)')               
**             call APRT(np1d,n,n,A,'Coefficient Matrix(i,j)') 
               call SOLVE (np1d,n,n,A,U,V,W,
     *                     RhsVec,R,ZVec,Phi,ES,pflg,epssol)
            else
               call SOLVE1(np1d,n,n,U,V,W,
     *                     RhsVec,R,Zvec,Phi,ES,pflg,epssol)
            endif
* Phi
            call lcolor(7,4)
            write(6,'(2a,2f8.3)') '   '//cond,' K, 1/K =',cK,1/cK
            call lcolor(4,0)
            call vprt(n,Phi,'Phi(j) : solutions')
* Phi,Psi,q-Calculated
            do j=1,n
               CVel=-1+CVelocity(z(j),n,zeta,Phi,cK,PsiB,LmbA,LmbI)
               thj=atan2(imag(zeta(j)-zeta(j+1)),
     *                   real(zeta(j)-zeta(j+1)))
               qcal(j)=-real(CVel)*cos(thj)+imag(CVel)*sin(thj)
               CPot=-z(j)+CPotentOn(z(j),n,zeta,Phi,
     *                            cK,PsiB,LmbA,LmbI)
               Phical(j)=real(CPot)
               Psical(j)=imag(CPot)
            enddo
            do j=1,N
               ds(j)=abs(zeta(j+1)-zeta(j))
            enddo
            qcald(1)=(Phi(2)-Phi(1))/(0.5*(ds(2)+ds(1)))
            do j=2,N-1
               qcald(j)=(Phi(j+1)-Phi(j-1))/
     *                  (ds(j)+0.5*(ds(j+1)+ds(j-1)))
            enddo
            qcald(N)=(Phi(N)-Phi(N-1))/(0.5*(ds(N)+ds(N-1)))
            call lcolor(3,0)
            write(6,*) 'Enter y to print calculated Phi, Psi '//
     *                 'on the body surface'
            write(6,*) '      RETURN to skip'
            read(5,'(a)') yorn
            if(yorn.eq.'y') then
               call lcolor(7,4)
               write(6,'(2a,2f8.3)') '   '//cond,' K, 1/K =',cK,1/cK
               call lcolor(5,4)
               call vprt(n,PhiCal,'Calculated Phi(j) on the body')
               write(6,'(/a,f10.3)') 'The following values must be '//
     *              'equal to PsiB =',PsiB
               call vprt(n,PsiCal,'Calculated Psi(j) on the body')
               call vprt(n,qcal,  'qcal(j) by CVelocity')
               call lcolor(7,2)
               write(6,*) '*** CVelocity does not give correct values'//
     *                    ' near body surface. ***'
               call lcolor(5,4)
               call vprt(n,qcald,'qcald(j)=dPhi/ds')
               write(6,*) 'The derivatives of Phi give correct values'//
     *                    ', compared with the ones by q-method.'
            endif
* Values at some points on free surface
            call lcolor(7,4)
            write(6,'(2a,2f8.3)') '   '//cond,' K, 1/K =',cK,1/cK
            write(6,'(a,3f8.3)') ' LmbA,PsiB,FscI  =',LmbA,PsiB,FSCI
            write(6,'(a,3f8.3)') '  K*etaA,K*etaF  =',YKA,YKF
            write(6,'(a,3f8.3)') '    etaA,  etaF  =',
     *                                       YKA/cK,YKF/cK
            write(6,'(a,3f8.3)') '      KyA,KyF    =',
     *                                       cK*(PsiB-LmbA),cK*PsiB
            call lcolor(3,0)
            write(6,*) 'Enter y to print LambdaA,I,F '//
     *                 'on the free surface'
            write(6,*) '      RETURN to skip'
            read(5,'(a)') yorn
            if(yorn.eq.'y') then
               call lcolor(7,4)
               write(6,'(2a,2f8.3)') '   '//cond,' K, 1/K =',cK,1/cK
               call FreeSCond(n,zeta,Phi,cK,PsiB,LmbF,LmbA,LmbI)
            endif
            goto 30
 40      continue
         goto 10
 20   continue
      goto 100
 110  continue
      call lcolor(0,0)
      end
************************************************************************
      subroutine FreeSCond
     *        (n,zeta,Phi,cK,PsiB,LmbF,LmbA,LmbI)
*
      real    Phi(*)
      real    LmbA,LmbI,LmbF
      complex zsamp,zeta(*)
*
      call lcolor(5,4)
* on FA (After free surface)
      write(6,'(a,f7.3)') 'On FA : given  -K*LmbA is',-cK*LmbA
      write(6,'(a)') '    x     K*Eta(u) K*psi -K*LmbA'
      do xi=-5,-1,1
         if(xi.eq.-1) then
            zsamp=cmplx(-1.001,0)
         else
            zsamp=cmplx(xi,0)
         endif
         call samplpnt(zsamp,n,zeta,Phi,cK,PsiB,LmbA,LmbI)
      enddo
* on FI (Inside free surface)
      write(6,'(a,f7.3)') 'On FI : given  -K*FscI is',-cK*(PsiB+LmbI)
      write(6,'(a)') '    x     K*Eta(u) K*psi -K*FscI'
      do xi=-1,1,0.5
         if(xi.eq.-1) then
            zsamp=cmplx(-0.999,0)
         elseif(xi.eq.1) then
            zsamp=cmplx( 0.999,0)
         else
            zsamp=cmplx(xi,0)
         endif
         call samplpnt(zsamp,n,zeta,Phi,cK,PsiB,LmbA,LmbI)
      enddo
* on FF (Fore free surface)
      write(6,'(a,f7.3)') 'On FF : given  -K*LmbF is',-cK*LmbF
      write(6,'(a)') '    x     K*Eta(u) K*psi -K*LmbF'
      do xi=1,5,1
         if(xi.eq.1) then
            zsamp=cmplx(1.001,0)
         else
            zsamp=cmplx(xi,0)
         endif
         call samplpnt(zsamp,n,zeta,Phi,cK,PsiB,LmbA,LmbI)
      enddo
      end
************************************************************************
      Subroutine samplpnt (z,n,zeta,Phi,K,PsiB,LmbA,LmbI)
*
      real    K,Phi(*)
      real    LmbA,LmbI
      complex i/(0,1)/
      complex zeta(*)
      complex z,cf,cv,FSC
      complex CPotent,CVelocity
*
      cf =  CPotent(z,n,zeta,Phi,K,PsiB,LmbA,LmbI)
      cv =CVelocity(z,n,zeta,Phi,K,PsiB,LmbA,LmbI)
      FSC=cv+i*K*cf
      write(6,'(4f8.3)') real(z),real(cv),K*imag(cf),real(FSC)
      end
************************************************************************
      Subroutine CoeMat(np1d,n,A,cK,z,zeta)
*
      real    A(np1d,*)
      complex z(*),zeta(*),zetaM
      complex WGNKfunc,sWG,WG2,WG1,WGNp1
      pi=acos(0.0)*2
      pi2inv=1/(2*pi)
      zetaM=(0,0)
*
      do i=1,np1d
         do j=1,np1d
            A(i,j)=0
         enddo
      enddo
      do i=1,n
         WG2=WGNKfunc(z(i),zeta(1),cK,zetaM,swG)
         do j=1,n
            WG1=WG2
            WG2=WGNKfunc(z(i),zeta(j+1),cK,zetaM,swG)
            if(i.eq.j) then
               A(i,j)=1-pi2inv*real(WG2-WG1)
            else
               A(i,j)= -pi2inv*real(WG2-WG1)
            endif
         enddo
      enddo
* Gamma Correction Part
      do i=1,n
         WG1  =WGNKfunc(z(i),zeta(1),  cK,zetaM,swG)
         WGNp1=WGNKfunc(z(i),zeta(n+1),cK,zetaM,swG)
         A(i,1)=A(i,1)-pi2inv*real(WG1)
         A(i,n)=A(i,n)+pi2inv*real(WGNp1)
      enddo
      end
************************************************************************
      subroutine RhsVecC(n,RhsVec,cK,PsiB,LmbA,LmbI,z,zeta)
*
      real    RhsVec(*)
      complex z(*),zeta(*)
      real    LmbA,LmbI
      complex WQfunc,WQf,WQFPi,WQAPi
      pi=acos(0.0)*2
*
      pi2inv=1/(2*pi)
      thetacut=pi/2
      do i=1,n
         RhsVec(i)=0
      enddo
      do i=1,n
         WQFPi=pi2inv*WQfunc(z(i),zeta(1),  cK,thetacut,WQf)
         WQAPi=pi2inv*WQfunc(z(i),zeta(n+1),cK,thetacut,WQf)
**       WQFPi=-pi2inv*WQfunc(z(i),zeta(1),  cK,thetacut,WQf)
**       WQAPi=-pi2inv*WQfunc(z(i),zeta(n+1),cK,thetacut,WQf)
         RhsVec(i)=-real(z(i))
     *             -(LmbI+PsiB)     *real(WQFPi)
     *             +(LmbI+PsiB-LmbA)*real(WQAPi)
      enddo
      end
************************************************************************
      complex function CPotent(z,n,zeta,Phi,K,PsiB,LmbA,LmbI)
*
*     Perturbed Complex Potential around the Body
*     
      real    K 
      complex i/(0,1)/
      complex WGNKfunc,sWG, WGFPi,WGAPi, WG1,WG2
      complex WGfunc,LogNK,VLog
      complex WQfunc,sWQ, WQFPi,WQAPi 
      complex z,zeta(*),zetaM
      real    LmbA,LmbI
      real    Phi(*) 
      pi=acos(0.0)*2 
      pi2Inv=1/(pi*2) 
      thetacut=pi/2 
      zetaM=(0,0)
* 
      WQFPi=WQfunc(z,zeta(1),  K,thetacut,sWQ) 
      WQAPi=WQfunc(z,zeta(n+1),K,thetacut,sWQ) 
* 
      WGFPi=WGNKfunc(z,zeta(1),  K,zetaM,sWG)
      WGAPi=WGNKfunc(z,zeta(n+1),K,zetaM,sWG)
      CPotent=-pi2Inv* (PsiB+LmbI)      *WQFPi
     *        +pi2Inv* (PsiB+LmbI-LmbA) *WQAPi
     *        +pi2Inv*  Phi(1)          *WGFPi
     *        -pi2Inv*  Phi(n)          *WGAPi
      WG2  =WGfunc(z,zeta(1),  K,thetacut,sWG)
      do j=1,n 
         WG1=WG2-i*LogNK(z,zeta(j),zeta(j+1))+i*VLog(z-zeta(j))
         WG2=WGfunc(z,zeta(j+1),  K,thetacut,sWG)
         CPotent=CPotent+pi2Inv* Phi(j) *(WG2-WG1)
      enddo
      end 
************************************************************************
      complex function CPotentOn(z,n,zeta,Phi,K,PsiB,LmbA,LmbI)
*
*     Perturbed Complex Potential ON the Body
*     
      real    K 
      complex WGNKfunc,sWG, WGFPi,WGAPi, WG1,WG2
      complex WGfunc
      complex WQfunc,sWQ, WQFPi,WQAPi
      complex CPotent
      complex z,zeta(*),zetaM
      real    LmbA,LmbI
      real    Phi(*) 
      pi=acos(0.0)*2 
      pi2Inv=1/(pi*2) 
      thetacut=pi/2 
      zetaM=(0,0)
* 
      WQFPi=WQfunc(z,zeta(1),  K,thetacut,sWQ) 
      WQAPi=WQfunc(z,zeta(n+1),K,thetacut,sWQ) 
* 
      WGFPi=WGNKfunc(z,zeta(1),  K,zetaM,sWG)
      WGAPi=WGNKfunc(z,zeta(n+1),K,zetaM,sWG)
      CPotent=-pi2Inv* (PsiB+LmbI)      *WQFPi
     *        +pi2Inv* (PsiB+LmbI-LmbA) *WQAPi
     *        +pi2Inv*  Phi(1)          *WGFPi
     *        -pi2Inv*  Phi(n)          *WGAPi
      WG2  =WGfunc(z,zeta(1),  K,thetacut,sWG)
      do j=1,n 
         WG1=WG2
         WG2=WGfunc(z,zeta(j+1),  K,thetacut,sWG)
         CPotent=CPotent+pi2Inv* Phi(j) *(WG2-WG1)
      enddo
      CPotentOn=CPotent
      end 
***********************************************************************
      complex function CVelocity(z,n,zeta,Phi,K,PsiB,LmbA,LmbI)
*
*     Perturbed Complex Volocity ( u - i * v )around the Body
*     
      real    K
      complex Wmufunc,Wmuf, VGFPi,VGApi, VG1,VG2
      complex Wmfunc, Wmf,  VQFPi,VQAPi
      complex z,zeta(*)
      real    LmbA,LmbI
      real    Phi(*)
      pi=acos(0.0)*2
      pi2Inv=1/(pi*2)
*
      VQFPi=-Wmfunc (z,zeta(1),  K,Wmf)
      VQAPi=-Wmfunc (z,zeta(n+1),K,Wmf)
      VGFPi=-Wmufunc(z,zeta(1),  K,Wmf)
      VGAPi=-Wmufunc(z,zeta(n+1),K,Wmf)
      CVelocity=-pi2Inv*(LmbI+PsiB)     *VQFPi
     *          +pi2inv*(LmbI+PsiB-LmbA)*VQAPi
     *          +pi2inv* Phi(1)         *VGFPi
     *          -pi2inv* Phi(n)         *VGAPi
      VG2=-Wmufunc(z,zeta(1),  K,Wmuf)
      do j=1,n
         VG1=VG2
         VG2=-Wmufunc(z,zeta(j+1),  K,Wmuf)
         CVelocity=CVelocity+pi2Inv*Phi(j)*(VG2-VG1)
      enddo
      end
************************************************************************
      Subroutine BodyCdn(n,z,zeta)
*     
*     Co-Ordinate for a Body Section (Clockwise)
*  
      complex z(*),zeta(*)
      complex i/(0,1)/
      pi=acos(0.0)*2
*
* Test for Elliptic Body
**    i=i
**    a=1
**    b=1.2
*
      np1=n+1
      dth=pi/n
      do j=1,np1 
         th0=dth*(j-1)
         th=pi/2*(cos(th0)-1)
         zeta(j)=exp(i*th)
**       xj=a*cos(th)
**       yj=b*sin(th)
**       zeta(j)=cmplx(xj,yj)
      enddo
      do j=1,n
         z(j)=(zeta(j)+zeta(j+1))/2
      enddo
      end                                                               
************************************************************************
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
      write(6,*)
*                                                                       
  100 FORMAT(/5X,A)                                                 
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
      SUBROUTINE SOLVE(MD,MT,M1,A,U,V,W,G,R,Z,S,ES,PFLG,EPS)            
*                                                                       
*     TO SOLVE A*S=G BY MEANS OF SVD METHOD                             
*         VERSION 0.1                                                   
*                                                                       
      DIMENSION A(MD,*),U(MD,*),V(MD,*),W(*),G(*),R(*),Z(*)             
      DIMENSION S(*),ES(*)                                              
      LOGICAL TRUE/.TRUE./                                              
      LOGICAL PFLG                                                      
*                                                                       
*     SVD METHOD                                                        
*                                                                       
      CALL SVD(MD,MT,M1,A,W,TRUE,U,TRUE,V,IERR,R)                       
*                                                                       
*     IERR,U,V,W, PRINT OUT                                             
*                                                                       
      IF(PFLG) THEN                                                     
**       CALL APRT(MD,M1,M1,V,'V(I,J)  ')                                
      ENDIF                                                             
*                                                                       
*     ***  GIVE RHS, G, ONLY                                            
*                                                                       
      ENTRY SOLVE1 (MD,MT,M1,U,V,W,G,R,Z,S,ES,PFLG,EPS)
*     
*     TRANSPOSED(U)*G TO R                                              
*                                                                       
      DO I=1,MT                                                      
         T=0                                                               
         DO J=1,MT                                                      
            T=T+U(J,I)*G(J)                                                   
         enddo
         R(I)=T                                                            
      enddo
      call lcolor(2,0)
      WRITE(6,'(5X,''IERR  ='',I4,''  from SVD'')') IERR  
      if(PFLG) then
         CALL VPRT(M1,W,'W(I)    ')
         CALL VPRT(M1,R,'R(I)    ')    
      endif
*                                                                       
*     SOLUTION FOR  W*Z=R                                               
*     CHECK FOR EIGEN SOLUTION                                          
*                                                                       
      DO I=1,M1                                                      
         Z(I)=0.0                                                          
         IF(W(I).gt.EPS) then
            Z(I)=R(I)/W(I)                                                    
         else
            WRITE (6,'(/a,I5,a,2e12.3)') '     ',
     *                    I,'-th is Eigen Vector W(i),R(i) =',W(I),R(I) 
**          IF(PFLG) then
               DO  J=1,M1                                                      
                  ES(J)=V(J,I)                            
               enddo
               CALL VPRT(M1,ES,'ES(I)   ') 
**          endif
         endif                            
      enddo
*     
*     SOLUTION FOR V*S=Z                                                
*                                                                       
      DO I=1,M1                                                      
         T=0.0                                                             
         DO J=1,M1                                                      
            T=T+V(I,J)*Z(J) 
         enddo
         S(I)=T 
      enddo                                                           
      END                                                               
************************************************************************
      SUBROUTINE SVD(NM,M,N,A,W,MATU,U,MATV,V,IERR,RV1)                 
*                                                                       
      INTEGER I,J,K,L,M,N,II,I1,KK,K1,LL,L1,MN,NM,ITS,IERR              
      REAL A(NM,*),W(*),U(NM,*),V(NM,*),RV1(*)                          
      REAL C,F,G,H,S,X,Y,Z,SCALE,ANORM                                  
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
************************************************************************
***  WQfunc,  Wmfunc,  Vmfunc     
***  WGfunc,  Wmufunc, Vmufunc
***  WGHFfunc,  WGHFDfunc      : WGfunc with spetial cut for hydro-foil
***  WGNKfunc         : WGfunc with spetial cut for semi-submerged body
***  WGdfunc, VGdfunc : A pair of wave vortex
***  WGintNK, VGintNK, LogNK, VLog
***  = WGint, = VGint
***  WGintHF, VGintHF, LogHF
***  Expint  
************************************************************************
      complex function WQfunc(z,zeta,K,ThetaCut,sWQ)
*
*     ThetaCut : Angle of Cut of Log(z-zeta) must be POSITIVE
*
*  ThetaCut - 2 * Pi <     Argument of Log(z-zeta)     =< ThetaCut 
*                   .lt.                              .le.
*           - 3/2 Pi < Argument of Log(z-zetaBar) & E1 =< Pi/2
*
*    0 < K < 50  : Usual Wave Making Condition
*        K >= 50 : Limit Case of Low Speed ( Mirror Image Flow)
*        K =  0  : Limit Case of High Speed ( Inverse Mirror Image Flow)
*        K <  0  : Infinite Region Flow
*
      real    K
      complex i/(0,1)/
      complex z,zeta,zetaBar,miKZ,E1
      complex LogZ,LogZBar,EmiKZ,Skappa,sWQ
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
      if(K.lt.0) then
         sWQ=0
         WQfunc=LogZ
      elseif(K.eq.0) then
         sWQ   =    -LogZBar
         WQfunc=LogZ-LogZBar
      elseif(K.lt.50) then
         miKZ=-i*K*(z-zetaBar)
         EmiKZ=exp(miKZ)
         call expint(miKZ,E1)
         xsign=real(z-zeta)
         if(xsign.gt.0) then
            Skappa=EmiKZ*E1
         else
            Skappa=EmiKZ*E1+pi2*i*EmiKZ
         endif
         sWQ   =     LogZBar+2*Skappa
         WQfunc=LogZ+LogZBar+2*Skappa
      else
         sWQ   =     LogZBar
         WQfunc=LogZ+LogZBar
      endif
      end
************************************************************************
      complex function Wmfunc(z,zeta,K,sWm)
*
*    0 < K < 50  : Usual Wave Making Condition
*        K >= 50 : Limit Case of Low Speed ( Mirror Image Flow)
*        K =  0  : Limit Case of High Speed ( Inverse Mirror Image Flow)
*        K <  0  : Infinite Region Flow
*
      real    K
      complex i/(0,1)/
      complex z,zeta,zetaBar,miKZ,E1
      complex InvZ,InvZBar,EmiKZ,Skappa,sWm
      pi=acos(0.0)*2
      pi2=2*pi
*
      InvZ=1/(z-zeta)
      zetaBar=conjg(zeta)
      InvZBar=1/(z-zetaBar)
*
      if(K.lt.0) then
         sWm=0
         Wmfunc=-InvZ
      elseif(K.eq.0) then
         sWm   =      InvZBar
         Wmfunc=-InvZ+InvZBar
      elseif(K.lt.50) then
         miKZ=-i*K*(z-zetaBar)
         EmiKZ=exp(miKZ)
         call expint(miKZ,E1)
         xsign=real(z-zeta)
         if(xsign.ge.0) then
            Skappa=EmiKZ*E1
         else
            Skappa=EmiKZ*E1+pi2*i*EmiKZ
         endif
         sWm   =      InvZBar+2*i*K*Skappa
         Wmfunc=-InvZ+InvZBar+2*i*K*Skappa
      else
         sWm   =     -InvZBar
         Wmfunc=-InvZ-InvZBar
      endif
      end
************************************************************************
      complex function Vmfunc(z,zeta,K,sVm)
*
*    0 < K < 50  : Usual Wave Making Condition
*        K >= 50 : Limit Case of Low Speed ( Mirror Image Flow)
*        K =  0  : Limit Case of High Speed ( Inverse Mirror Image Flow)
*        K <  0  : Infinite Region Flow
*
      real    K
      complex i/(0,1)/
      complex z,zeta,zetaBar,miKZ,E1
      complex InvZ2,InvZBar,InvZBar2,EmiKZ,Skappa,sVm
      pi=acos(0.0)*2
      pi2=2*pi
*
      InvZ2=   1/(z-zeta)**2
      zetaBar=conjg(zeta)
      InvZBar= 1/(z-zetaBar)
      InvZBar2=1/(z-zetaBar)**2
*     
      miKZ=-i*K*(z-zetaBar)
      EmiKZ=exp(miKZ)
      call expint(miKZ,E1)
      xsign=real(z-zeta)
      if(xsign.ge.0) then
         Skappa=EmiKZ*E1
      else
         Skappa=EmiKZ*E1+pi2*i*EmiKZ
      endif
      sVm=        -InvZBar2-2*K*i*InvZBar+2*K**2*Skappa
      Vmfunc=InvZ2-InvZBar2-2*K*i*InvZBar+2*K**2*Skappa
      end



************************************************************************
      complex function WGfunc(z,zeta,K,ThetaCut,sWG)
*
*    0 < K < 50  : Usual Wave Making Condition
*        K >= 50 : Limit Case of Low Speed ( Mirror Image Flow)
*        K =  0  : Limit Case of High Speed ( Inverse Mirror Image Flow)
*        K <  0  : Infinite Region Flow
*
*     ThetaCut : Angle of Cut of Log(z-zeta) must be POSITIVE
*
*  ThetaCut - 2 * Pi <     Argument of Log(z-zeta)     =< ThetaCut 
*                   .lt.                              .le.
*           - 3/2 Pi < Argument of Log(z-zetaBar) & E1 =< Pi/2
*
*
      real    K
      complex i/(0,1)/
      complex z,zeta,zetaBar,miKZ,E1
      complex LogZ,LogZBar,EmiKZ,Skappa,sWG
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
      if(K.lt.0) then
         WGfunc=-i*LogZ
         sWG=0
      elseif(K.eq.0) then
         sWG   =       -i*LogZBar
         WGfunc=-i*LogZ-i*LogZBar
      elseif(K.lt.50) then
         miKZ=-i*K*(z-zetaBar)
         EmiKZ=exp(miKZ)
         call expint(miKZ,E1)
         xsign=real(z-zeta)
         if(xsign.gt.0) then
            Skappa=EmiKZ*E1
         else
            Skappa=EmiKZ*E1+pi2*i*EmiKZ
         endif
         sWG   =        i*LogZBar+2*i*Skappa
         WGfunc=-i*LogZ+i*LogZBar+2*i*Skappa
      else
         sWG   =        i*LogZBar
         WGfunc=-i*LogZ+i*LogZBar
      endif
      end
************************************************************************
      complex function Wmufunc(z,zeta,K,sWmu)
*
*    0 < K < 50  : Usual Wave Making Condition
*        K >= 50 : Limit Case of Low Speed ( Mirror Image Flow)
*        K =  0  : Limit Case of High Speed ( Inverse Mirror Image Flow)
*        K <  0  : Infinite Region Flow
*
      real    K
      complex i/(0,1)/
      complex z,zeta,zetaBar,miKZ,E1
      complex InvZ,InvZBar,EmiKZ,Skappa,sWmu
      pi=acos(0.0)*2
      pi2=2*pi
*
      InvZ=1/(z-zeta)
      zetaBar=conjg(zeta)
      InvZBar=1/(z-zetaBar)
*
      if(K.lt.0) then
         sWmu=0
         Wmufunc=i*InvZ
      elseif(K.eq.0) then
         Wmufunc=i*InvZ+i*InvZBar
         sWmu=          i*InvZBar
      elseif(K.lt.50) then
         miKZ=-i*K*(z-zetaBar)
         EmiKZ=exp(miKZ)
         call expint(miKZ,E1)
         xsign=real(z-zeta)
         if(xsign.gt.0) then
            Skappa=EmiKZ*E1
         else
            Skappa=EmiKZ*E1+pi2*i*EmiKZ
         endif
         Wmufunc=i*InvZ+i*InvZBar-2*K*Skappa
         sWmu   =       i*InvZBar-2*K*Skappa
      else
         Wmufunc=i*InvZ-i*InvZBar
         sWmu   =      -i*InvZBar
      endif
      end
**************************************************************************
      complex function Vmufunc(z,zeta,K,sVmu)
*
*    0 < K < 50  : Usual Wave Making Condition
*        K >= 50 : Limit Case of Low Speed ( Mirror Image Flow)
*        K =  0  : Limit Case of High Speed ( Inverse Mirror Image Flow)
*        K <  0  : Infinite Region Flow
*
      real    K
      complex i/(0,1)/
      complex z,zeta,zetaBar,miKZ,E1
      complex InvZ2,InvZBar,InvZBar2,EmiKZ,Skappa,sVmu
      pi=acos(0.0)*2
      pi2=2*pi
*
      InvZ2=   1/(z-zeta)**2
      zetaBar=conjg(zeta)
      InvZBar= 1/(z-zetaBar)
      InvZBar2=1/(z-zetaBar)**2
*
      miKZ=-i*K*(z-zetaBar)
      EmiKZ=exp(miKZ)
      call expint(miKZ,E1)
      xsign=real(z-zeta)
      if(xsign.ge.0) then
         Skappa=EmiKZ*E1
      else
         Skappa=EmiKZ*E1+pi2*i*EmiKZ
      endif
      sVmu   =        -i*InvZBar2+2*K*InvZBar+2*i*K**2*Skappa
      Vmufunc=-i*InvZ2-i*InvZBar2+2*K*InvZBar+2*i*K**2*Skappa
      end





************************************************************************
      complex function WGHFfunc(z,zeta,K,zetaE,sWG)
*
*     Cut of Log(z-zeta) is set as
*          (-Inf,etaE) - zetaE - zeta
*
*    0 < K < 50  : Usual Wave Making Condition
*        K >= 50 : Limit Case of Low Speed ( Mirror Image Flow)
*        K =  0  : Limit Case of High Speed ( Inverse Mirror Image Flow)
*        K <  0  : Infinite Region Flow
*
      real    K
      complex i/(0,1)/
      complex z,zeta,zetaE,zetaBar,miKZ,E1
      complex LogZ,LogZBar,EmiKZ,Skappa,sWG
      pi=acos(0.0)*2
      pi2=2*pi
      pih=pi/2
*
      LogZ=log(z-zeta)
      Alog=real(LogZ)
      ArgZ=imag(LogZ)
      x=real(z)
      y=imag(z)
      xsi=real(zeta)
      eta=imag(zeta)
      xsiE=real(zetaE)
      etaE=imag(zetaE)
      if(x.lt.xsiE) then
         if(y.ge.etaE) then
            if(ArgZ.lt.0) then
               ArgZ=ArgZ+pi2
            endif
         else
            if(ArgZ.gt.0) then
               ArgZ=ArgZ-pi2
            endif
         endif
      else
         if(x.lt.xsi) then
            ul=(y-etaE)*(xsi-xsiE)-(eta-etaE)*(x-xsiE)
            if(ul.ge.0) then
               if(ArgZ.lt.0) then
                  ArgZ=ArgZ+pi2
               endif
            else
               if(ArgZ.gt.0) then
                  ArgZ=ArgZ-pi2
               endif
            endif
         endif
      endif
      LogZ=cmplx(ALog,ArgZ)
*
      zetaBar=conjg(zeta)
      LogZBar=log(z-zetaBar)
      Alog=real(LogZBar)
      ArgZ=imag(LogZBar)
      if(ArgZ.gt.pih) ArgZ=ArgZ-pi2
      LogZBar=cmplx(ALog,ArgZ)
      if(K.lt.0)  then
         WGHFfunc=-i*LogZ
         sWG=0
      elseif(K.eq.0)  then
         WGHFfunc=-i*LogZ-i*LogZBar
         sWG     =       -i*LogZBar
      elseif(K.lt.50) then
         miKZ=-i*K*(z-zetaBar)
         EmiKZ=exp(miKZ)
         call expint(miKZ,E1)
         xsign=real(z-zeta)
         if(xsign.gt.0) then
            Skappa=EmiKZ*E1
         else
            Skappa=EmiKZ*E1+pi2*i*EmiKZ
         endif
         sWG     =        i*LogZBar+2*i*Skappa
         WGHFfunc=-i*LogZ+i*LogZBar+2*i*Skappa
      else
         sWG     =        i*LogZBar
         WGHFfunc=-i*LogZ+i*LogZBar
      endif
      end


************************************************************************
      complex function WGHFDfunc(z,zeta,K,zetaM,zetaE,swG)
*
*     Cut of Log(z-zeta) is set as
*          (-Inf,etaE) - zetaE - zetaM - zeta
*
*    0 < K < 50  : Usual Wave Making Condition
*        K >= 50 : Limit Case of Low Speed ( Mirror Image Flow)
*        K =  0  : Limit Case of High Speed ( Inverse Mirror Image Flow)
*        K <  0  : Infinite Region Flow
*
      real    K
      complex i/(0,1)/
      complex z,zeta,zetaE,zetaM,zetaBar,miKZ,E1
      complex LogHF,LogZ,LogZBar,EmiKZ,Skappa,swG
      
      pi=acos(0.0)*2
      pi2=2*pi
      pih=pi/2
*
      LogZ=LogHF(z,zeta,zetaM,zetaE)
*
      zetaBar=conjg(zeta)
      LogZBar=log(z-zetaBar)
      Alog=real(LogZBar)
      ArgZ=imag(LogZBar)
      if(ArgZ.gt.pih) ArgZ=ArgZ-pi2
      LogZBar=cmplx(ALog,ArgZ)
      if(K.lt.0)  then
         swG=0
         WGHFDfunc=-i*LogZ
      elseif(K.eq.0)  then
         swG      =       -i*LogZBar
         WGHFDfunc=-i*LogZ-i*LogZBar
      elseif(K.lt.50) then
         miKZ=-i*K*(z-zetaBar)
         EmiKZ=exp(miKZ)
         call expint(miKZ,E1)
         xsign=real(z-zeta)
         if(xsign.gt.0) then
            Skappa=EmiKZ*E1
         else
            Skappa=EmiKZ*E1+pi2*i*EmiKZ
         endif
         swG      =        i*LogZBar+2*i*Skappa
         WGHFDfunc=-i*LogZ+i*LogZBar+2*i*Skappa
      else
         swG      =        i*LogZBar
         WGHFDfunc=-i*LogZ+i*LogZBar
      endif
      end


************************************************************************
      complex function WGNKfunc(z,zeta,K,zetaM,sWG)
*
*     Wave Vortex with cut of LogNK
*
*    0 < K < 50  : Usual Wave Making Condition
*        K >= 50 : Limit Case of Low Speed ( Mirror Image Flow)
*        K =  0  : Limit Case of High Speed ( Inverse Mirror Image Flow)
*        K <  0  : Infinite Region Flow
*
*     Cut of log(z-zeta) is set as
*        (xsiM,inf) - zeta - zeta
*                                  
      real    K
      complex i/(0,1)/
      complex z,zeta,zetaM,zetaBar,miKZ,E1,LogNK
      complex LogZ,LogZBar,EmiKZ,SKappa,swG
      pi=acos(0.0)*2
      pi2=2*pi
      pih=pi/2
*
      LogZ=LogNK(z,zeta,zetaM)
*
      zetaBar=conjg(zeta)
      LogZBar=log(z-zetaBar)
      Alog=real(LogZBar)
      ArgZ=imag(LogZBar)
      if(ArgZ.gt.pih) ArgZ=ArgZ-pi2
      LogZBar=cmplx(ALog,ArgZ)
*
      if(K.lt.0) then
         swG     = 0
         WGNKfunc=-i*LogZ
      elseif(K.eq.0) then
         swG     =       -i*LogZBar
         WGNKfunc=-i*LogZ-i*LogZBar
      elseif(K.lt.50) then
         miKZ=-i*K*(z-zetaBar)
         EmiKZ=exp(miKZ)
         call expint(miKZ,E1)
         xsign=real(z-zeta)
         if(xsign.gt.0) then
            Skappa=EmiKZ*E1
         else
            Skappa=EmiKZ*E1+pi2*i*EmiKZ
         endif
         swG     =        i*LogZBar+2*i*Skappa
         WGNKfunc=-i*LogZ+i*LogZBar+2*i*Skappa
      else
         swG=i*LogZBar
         WGNKfunc=-i*LogZ+swG
      endif
      end



***********************************************************************
      complex function WGdfunc(z,zeta2,zeta1,K)
*
*     a pair of wave VORTEX WG(a,zeta2) - WG(z,zeta1)
*
*     Cut :  zeta1 -- zeta2
*
      real    K
      complex WG1,WG2,swG1,swG2
      complex WGNKfunc
      complex z,zeta2,zeta1
      complex dz /(0,0.000001)/
*
*  for zeta1
      WG1=WGNKfunc(z,zeta1,K,zeta2,swG1)
*  for zeta2
**    WG2=WGNKfunc(z,zeta2,K,zeta2,swG2)
      WG2=WGNKfunc(z,zeta2,K,zeta2+dz,swG2)
*  Difference
      WGdfunc=WG2-WG1
      end
***********************************************************************
      complex function VGdfunc(z,zeta2,zeta1,K)
*
*     Complex Velocity due to
*          a couple of wave VORTEX WG(a,zeta2) - WG(z,zeta1)
*
      real    K
      complex VG1,VG2
      complex Wmufunc,Wmuf
      complex z,zeta2,zeta1
*
*  for zeta1
      VG1=-Wmufunc(z,zeta1,K,Wmuf)
*  for zeta2
      VG2=-Wmufunc(z,zeta2,K,Wmuf)
*  Difference
      VGdfunc=VG2-VG1
      end




************************************************************************
      complex function WGintNK(z,zeta2,zeta1,K,zetaM)
*                      WGintNK
*
*     The Revised Version    
*     
*          For a Flow aroud a Water-Surface-Piercing-Body
*     Integrated Wave Vortex Segment
*            with zeta1, zeta2 and zetaM located clockwisely
*     Cut of log(z-zeta) is set as
*        zeta1,2 -- zetaM -- (xsiM,etaE) -- (-inf,etaE)
*                                  etaE > 10
*     Cut of log(z-zetaBar) as
*        zeatBar -- (xsiBar,inf)
*
*     Cut of E1 as
*        zeatBar -- (xsiBar,inf)
*
*    0 < K < 50  : Usual Wave Making Condition
*        K >= 50 : Limit Case of Low Speed ( Mirror Image Flow)
*        K =  0  : Limit Case of High Speed ( Inverse Mirror Image Flow)
*        K <  0  : Infinite Region Flow
*
      real    K
      
      complex i/(0,1)/
      complex WGint1,WGint2,LogNK,VLog
      complex z,zeta1,zeta2,zetaM
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
      LogZ=LogNK(z,zeta2,zetaM)
      zdif=z-zeta2
*
      zetaBar=conjg(zeta2)
      zdifBar=z-zetaBar
      LogZBar=VLog(zdifBar)
      EiG=dzeta/abs(dzeta)
      if(K.lt.0)  then
         WGint2=i*conjg(EiG)*zdif*(LogZ-1)
      elseif(K.eq.0)  then
         WGint2=i*conjg(EiG)*zdif*(LogZ-1)+i*EiG*zdifBar*(LogZBar-1)
      elseif(K.lt.50) then
         miKz=-i*K*zdifBar
         EmiKz=exp(miKz)
         call expint(miKZ,E1)
         if(x-xsi2.gt.0) then
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
      LogZ=LogNK(z,zeta1,zetaM)
      zdif=z-zeta1
*
      zetaBar=conjg(zeta1)
      zdifBar=z-zetaBar
      LogZBar=VLog(zdifBar)
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
      WGintNK=WGint2-WGint1
      end
************************************************************************
      complex function VGintNK(z,zeta2,zeta1,K,zetaM)
*
*     The Revised Version    
*     
*                      VGintNK
*     Points zeta2 and zeta1 are located clockwisely
*     Cut of log(z-zeta) is set as
*        zeta -- zetaM -- (xsiM,inf)
*     Cut of log(z-zetaBar) & E1 as
*        zetaBar -- (xsiBar,inf)
*
*    0 < K < 50  : Usual Wave Making Condition
*        K >= 50 : Limit Case of Low Speed ( Mirror Image Flow)
*        K =  0  : Limit Case of High Speed ( Inverse Mirror Image Flow)
*        K <  0  : Infinite Region Flow
*
      real    K
      
      complex i/(0,1)/
      complex VGint1,VGint2,LogNK,VLog
      complex z,zeta1,zeta2,zetaM,zetaE
      complex dzeta,zetaBar,zdifBar
      complex LogZ,LogZBar
      complex EiG,miKz,EmiKz,E1,SKappa
      real    etaE/10/
      pi=acos(0.0)*2
      pi2=pi*2
*
      x=real(z)
      xsi1=real(zeta1)
      xsi2=real(zeta2)
      dzeta=zeta2-zeta1
*     For zetaE
      zetaE=conjg(zetaM)+i*etaE
*
*     For zeta2
*
      LogZ=LogNK(z,zeta2,zetaM,zetaE)
*
      zetaBar=conjg(zeta2)
      zdifBar=z-zetaBar
      LogZBar=VLog(zdifBar)
      EiG=dzeta/abs(dzeta)
      if(K.lt.0)  then
         VGint2=i*conjg(EiG)*LogZ
      elseif(K.eq.0)  then
         VGint2=i*conjg(EiG)*LogZ+i*EiG*LogZBar
      elseif(K.lt.50) then
         miKz=-i*K*zdifBar
         EmiKz=exp(miKz)
         call expint(miKZ,E1)
         if(x-xsi2.gt.0) then
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
      LogZ=LogNK(z,zeta1,zetaM,zetaE)
*
      zetaBar=conjg(zeta1)
      zdifBar=z-zetaBar
      LogZBar=VLog(zdifBar)
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
      VGintNK=VGint2-VGint1
      end
***************************************************************************
      complex function VLog(z)
*
*     Complex Logarithmic Function for Iamg(z) > 0
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
*     ( See Section 3.3.4 )
*
*     Cut of Log ; zeta - zetaM - (xiM,inf)
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
      complex function WGintHF(z,zeta2,zeta1,K,zetaM,zetaE)
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
*        zeteBar --(xsiBar,inf)
*
*    0 < K < 50  : Usual Wave Making Condition
*        K >= 50 : Limit Case of Low Speed ( Mirror Image Flow)
*        K =  0  : Limit Case of High Speed ( Inverse Mirror Image Flow)
*        K <  0  : Infinite Region Flow
*
      real    K
      complex i/(0,1)/
      complex WGint1,WGint2
      complex z,zeta1,zeta2,zetaM,zetaE
      complex dzeta,zetaBar,zdif,zdifBar
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
         if(x-xsi1.ge.0) then
            SKappa=EmiKz*E1
         else
            SKappa=EmiKz*E1+pi2*i*EmiKz
         endif
         WGint1=i*conjg(EiG)*zdif*(LogZ-1)-i*EiG*zdifBar*(LogZBar-1)
     *         +2/K*EiG*LogZBar+2/K*EiG*SKappa
      else
         WGint1=i*conjg(EiG)*zdif*(LogZ-1)-i*EiG*zdifBar*(LogZBar-1)
      endif
      WGintHF=WGint2-WGint1
      end
************************************************************************
      complex function VGintHF(z,zeta2,zeta1,K,zetaM,zetaE)
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
         if(x-xsi1.ge.0) then
            SKappa=EmiKz*E1
         else
            SKappa=EmiKz*E1+pi2*i*EmiKz
         endif
         VGint1=i*conjg(EiG)*LogZ-i*EiG*LogZBar
     *         -2*i*EiG*SKappa
      else
         VGint1=i*conjg(EiG)*LogZ-i*EiG*LogZBar
      endif
      VGintHF=VGint2-VGint1
      end
************************************************************************
      complex function LogHF(z,zeta,zetaM,zetaE)
*
*     Complex Logarithmic Function for Hydro-Foil ( See Section 3.3.4 )
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





************************************************************************
      complex function WGint(z,zeta2,zeta1,K,zetaM)
*                      WGintNK
*
      real    K
      complex z,zeta1,zeta2,zetaM
      complex WGintNK
*
      WGint=WGintNK(z,zeta2,zeta1,K,zetaM)
      end
************************************************************************
      complex function VGint(z,zeta2,zeta1,K,zetaM)
*                      VGintNK
*     
      real    K
      complex z,zeta1,zeta2,zetaM
      complex VGintNK
* 
      VGint=VGintNK(z,zeta2,zeta1,K,zetaM)
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

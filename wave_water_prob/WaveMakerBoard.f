*     Problem of Oscilating 2-D Wave-Maker in a Uniform Flow
*                  with Fore Flexible Wall
*                  To get Alpha-1 Wave only
*                 ________
*                .|      :\
*               . |      : \
*             .   |      :  \
*          .      |      :   \  Pressure Damping Zone
*    ___._________|      :    \__________________________________\
*    .           0      Lw    Ld           Lf                  x / 
*                 <--+--><--+-><--------+--->
*    Waves         Plate    |           |                <-- U
*                        Flexible Wall  |
*                               Pressure Damping Zone (Rigid Wall)
*
      parameter ( ND=500+1, N2D=ND*2 )
      parameter ( MD=1000+ND )
*
      common /ab12/alpha1,alpha2,beta1,beta2,sqop,csqom
      common /Omega/Omega,kappa,nu,Sigma,Fn,Umbys,somega,f
      common /WLen/WLena1,WLena2,WLenb1,WLenb2
*
      real    Nu,Kappa,NuI
      real    x(ND),xsi(ND),Eta(N2D)
      real    Eta1C(ND),Eta1S(ND)
      complex Eta1(ND)
      real    EtaxC(ND),EtaxS(ND)
      complex Etax(ND)
      real    p1C(ND),p1S(ND)
      complex p1(ND)
      real    pxC(ND),pxS(ND)
      complex px(ND)
      real    p2C(ND),p2S(ND)
      complex p2(ND)
      complex dEta1,dEtax,dEta2
      complex cEta1(MD),cEtax(MD),cEta2(MD)
      real    xWave(MD)
      real    A(N2D,N2D),p(N2D)
      complex csqom,beta1,beta2
      real    U(N2D,N2D),V(N2D,N2D),W(N2D),R(N2D),Z(N2D),ES(N2D)
      complex Ha1,Ha2,Hmax,Hmin,j/(0.0,1.0)/
      complex heaveHa1,heaveHa2
      complex pitchHa1,pitchHa2
      complex Heave,Pitch
      character yorn*1
      character LCol*1
      common   /LCol/LCol
      pi=acos(0.0)*2 
      rd=180/pi
*
      LCol='y'
**    LCol='n'
*
      ALwm =0.060
      dLdm=0.120
      ALdm=ALwm+dLdm
      ALd=ALdm/ALwm
      ALf=20
      ALw=1
      call lcolor(7,3)
      write(6,*) '****************************************************'
      write(6,*) 'Enter N ( 80 ) >'
      call lcolor(2,0)
      write(6,*) '  80     10    '
      read(5,*) N
      Np1=N+1
      N2=N*2
      N2p1=N2+1
      N2p2=N2+2
      call XCoordnt(N,x,xsi,Alf)
      indW=0
      indD=0
      do i=1,N
         if(indW.eq.0 .and. x(i).ge.ALw) then
            indW=1
            Kw=i-1
         elseif(indD.eq.0 .and. x(i).ge.ALd) then
            indD=1
            Kd=i-1
         endif
      enddo
 10   continue
         call lcolor(7,3)
         write(6,*) '*************************************************'
         write(6,*)
     *   'Enter Wave Number Nu=gLw/U**2   (   1.5     1     0.5  ) *'
         write(6,*)
     *     '                                 Slow           Fast'  
         write(6,*) 'Enter ''*'' to go out of the LOOP'
         read(5,*,err=20,end=20) NuI
         write(6,*)
     *   'Enter Omega                     (   1.5     2     2.5  ) *'
         write(6,*)  
     *   '                                   Slow          Rapid'
         read(5,*,end=20,err=20) OmegaI
         call ONtoKS(OmegaI,NuI,ALwm)
         Hzbys=1/f
         call lcolor(5,4)
         write(6,*) 'N = ',N
         write(6,'(a,2f10.4)') 'Lw(m),do/Lw   =',ALwm,Alw
         write(6,'(a,2f10.4)') 'Ld(m),do/Lw   =',ALdm,Ald
         write(6,'(a,2f10.4)') 'Lf(m),do/Lw   =',ALd*Alf,Alf
         call lcolor(7,5)
         write(6,'(a,f10.4)')  'U(m/s)  =',Umbys
         write(6,'(a,f10.4)')  'Hz      =',Hzbys
         if(Omega.le.0.25) then
            call lcolor(7,2)
            write(6,'(a,f10.4,a)') 'Omega(',Omega,') < 0.25 occurs'
         endif
**            _______   **
         call ab12etc
**            ~~~~~~~   **
         write(6,'(a,2f14.5)') 'Fn,    Omega  =',Fn,    Omega
         write(6,'(a,2f14.5)') 'Sigma, Nu     =',Sigma, Nu
         write(6,'(a,2f14.5)') 'Kappa         =',Kappa
         write(6,'(a,2f14.5)') 'alpha1,alpha2 =',alpha1,alpha2
         write(6,'(a,2f14.5)') 'beta1         =',beta1
         write(6,'(a,2f14.5)') 'beta2         =',beta2
         write(6,'(a,2f14.5)') 'WLa1/L,WLa2/L =',WLena1,WLena2
         write(6,'(a,2f14.5)') 'WLb1/L,WLb2/L =',WLenb1,WLenb2
** RHSVec     ________                                           **
         call YCoordnt(N,x,Eta1,Eta1C,Eta1S,Etax,EtaxC,EtaxS,ALd)
**            ~~~~~~~~                                           **
         call lcolor(3,0)
         write(6,*) '*************************************************'
         write(6,*) 'Enter y for print x-coordinates'
         write(6,*) '      RETURN to skip'
         read(5,'(a)') yorn
**       yorn='n'
         if(yorn.eq.'y') then
            call lcolor(5,4)
            write(6,'(a,3f10.4)') 'Lw,Ld,Lf =',  ALw,ALd,ALf
            write(6,'(a,2i10)')   '  Kw,Kd  =   ',Kw, Kd
            call vprt(Np1, xsi,  'Segment Points   : xsi(i)/Lw')
            call vprt(N,   x,    'Boundary Points  : x(i)/Lw')
         endif
         call lcolor(3,0)
         write(6,*) '*************************************************'
         write(6,*) 'Enter y for print y-coordinates'
         write(6,*) '      RETURN to skip'
         read(5,'(a)') yorn
**       yorn='n'
         if(yorn.eq.'y') then
            call lcolor(3,4)
            write(6,'(a,2i10)') '  Kw,Kd  =     ',Kw, Kd
            write(6,*) 'The following 2 vectors are RHS-vec. for heave'
            call vprt(N,   Eta1C,'Boundary Heights : Eta1C(i)/A0')
            call vprt(N,   Eta1S,'Boundary Heights : Eta1S(i)/A0')
            call lcolor(5,4)
            write(6,*) 'The following 2 vectors are RHS-vec. for pitch'
            call vprt(N,   EtaxC,'Boundary Heights : EtaxC(i)/A0')
            call vprt(N,   EtaxS,'Boundary Heights : EtaxS(i)/A0')
         endif
**            _______                        **
         call CoefMat(N2D,N,x,xsi,A)
**            ~~~~~~~                        **
         call lcolor(3,0)
         write(6,*) '*************************************************'
         write(6,*) 'Enter y for print CoeMat'
         write(6,*) '      RETURN to skip'
         read(5,'(a)') yorn
**       yorn='n'
         if(yorn.eq.'y') then
            call lcolor(4,0)
            call APRT (N2D,N2p2,N2p2,A,'Coefficient Matrix')
         endif
* For Heave(1)
         call lcolor(2,0)
         write(6,*) '*************************************************'
         write(6,*) 'Solution for Heave Motion'
         do i=1,N
            Eta(i)  =Eta1C(i)
            Eta(N+i)=Eta1S(i)
         enddo
         Eta(N2p1)=0
         Eta(N2p2)=0
**            _____                                     **
         CALL SOLVE (N2D,N2p2,N2p2,A,U,V,W,Eta,R,Z,p,ES,
**            ~~~~~                                     **
     *               .false.,1.0E-5)
         do i=1,N
            p1C(i)=p(i)
            p1S(i)=p(N+i)
            p1(i)=cmplx(p1C(i),p1S(i))
         enddo
         dEta1C=p(N2p1)
         dEta1S=p(N2p2)
         dEta1=cmplx(dEta1C,dEta1S)
         call lcolor(3,0)
         write(6,*) '*************************************************'
         write(6,*) 'Enter y to pront Pressure for Heave'
         write(6,*) '      RETURN to skip'
         read(5,'(a)') yorn
**       yorn='n'
         if(yorn.eq.'y') then
            call lcolor(4,0)
            call vprt(N2,p,'Pres. Distri. : p1C(i),p1S(i) for heave')
            write(6,'(a,2f10.3)') 'dEta1C,S =',dEta1C,dEta1S
         endif
         call WaveCal(N,x,xsi,p,Eta1C,Eta1S,
     *                Mx,xWave,cEta1)
*             _______
         call AmpFunc(N,xsi,p,
*             ~~~~~~~
     *                Ha1,Ha2,AHa1,AHa2,PHa1,PHa2)
         call lcolor(7,4)
         write(6,*) '*** Amplitude Functions for Heave ***'
         write(6,*) '   Halpha1             Halpha2 '
         write(6,'(6f10.4)') Ha1,Ha2
         write(6,'(6f10.4)') AHa1,PHa1,AHa2,PHa2
         heaveHa1=Ha1
         heaveHa2=Ha2
         call BeatAnl(PHa1,PHa2,WLBeat,xMax,xMin)
         call lcolor(4,0)
         write(6,'(a,f10.4)')  'Wave Length of Beat  =',WLBeat
         write(6,'(a,2f10.4)') 'xMax,Min/Lw   =',xMax,xMin
         Hmax=Ha1*exp(-j*alpha1*xMax)+Ha2*exp(-j*alpha2*xMax)
         AHmax=abs(Hmax)
         PHmax=atan2(imag(Hmax),real(Hmax))*rd
         Hmin=Ha1*exp(-j*alpha1*xMin)+Ha2*exp(-j*alpha2*xMin)
         AHmin=abs(Hmin)
         PHmin=atan2(imag(Hmin),real(Hmin))*rd
         call lcolor(7,4)
         write(6,*) '    HxMax               HxMin'
         write(6,'(6f10.4)') Hmax,Hmin
         write(6,'(6f10.4)') AHmax,PHmax,AHmin,PHmin
         call lcolor(3,0)
         write(6,*) '*************************************************'
         write(6,*) 'Enter y for pront Wave Components for Heave'
         write(6,*) '      RETURN to skip'
         read(5,'(a)') yorn
**       yorn='n'
         if(yorn.eq.'y') then
            call lcolor(7,4)
            write(6,*) '      xi     etaC(xi)  etaS(xi)'
            do Ix=251,495,10
               xI=-10+0.02*(Ix-1)
               write(6,'(3f10.3)') xI,cEta1(Ix)
            enddo
         endif
* For Pitch(x)
         call lcolor(2,0)
         write(6,*) '*************************************************'
         write(6,*) 'Solution for Pitch Motion'
         do i=1,N
            Eta(i)  =EtaxC(i)
            Eta(N+i)=EtaxS(i)
         enddo
         Eta(N2p1)=0
         Eta(N2p2)=0
**            ______                                      **
         CALL SOLVE1(N2D,N2p2,N2p2,  U,V,W,Eta,R,Z,p,ES,
**            ~~~~~~                                      **
     *               .false.,1.0E-5)
         do i=1,N
            pxC(i)=p(i)
            pxS(i)=p(N+i)
            px(i)=cmplx(pxC(i),pxS(i))
         enddo
         dEtaxC=p(n2p1)
         dEtaxS=p(n2p2)
         dEtax=cmplx(dEtaxC,dEtaxS)
         call lcolor(3,0)
         write(6,*) '*************************************************'
         write(6,*) 'Enter y to print Pressure for Pitch'
         write(6,*) '      RETURN to skip'
         read(5,'(a)') yorn
**       yorn='n'
         if(yorn.eq.'y') then
            call lcolor(4,0)
            call vprt(N2,p,'Pres. Distri. : pxC,pxS(i) for pitch')
            write(6,'(a,2f10.3)') 'dEtaxC,S =',dEtaxC,dEtaxS
         endif
         call WaveCal(N,x,xsi,p,EtaxC,EtaxS,
     *                Mx,xWave,cEtax)
*             _______
         call AmpFunc(N,xsi,p,
*             ~~~~~~~
     *                Ha1,Ha2,
     *                AHa1,AHa2,PHa1,PHa2)
         call lcolor(7,4)
         write(6,*) '*** Amplitude Functions for Pitch ***'
         write(6,*) '   Halpha1             Halpha2 '
         write(6,'(6f10.4)') Ha1,Ha2
         write(6,'(6f10.4)') AHa1,PHa1,AHa2,PHa2
         pitchHa1=Ha1
         pitchHa2=Ha2
         call BeatAnl(PHa1,PHa2,WLBeat,xMax,xMin)
         call lcolor(4,0)
         write(6,'(a,f10.4)')  'Wave Length of Beat  =',WLBeat
         write(6,'(a,2f10.4)') 'xMax,Min/Lw   =',xMax,xMin
         Hmax=Ha1*exp(-j*alpha1*xMax)+Ha2*exp(-j*alpha2*xMax)
         AHmax=abs(Hmax)
         PHmax=atan2(imag(Hmax),real(Hmax))*rd
         Hmin=Ha1*exp(-j*alpha1*xMin)+Ha2*exp(-j*alpha2*xMin)
         AHmin=abs(Hmin)
         PHmin=atan2(imag(Hmin),real(Hmin))*rd
         call lcolor(7,4)
         write(6,*) '    HxMax               HxMin'
         write(6,'(6f10.4)') Hmax,Hmin
         write(6,'(6f10.4)') AHmax,PHmax,AHmin,PHmin
         call lcolor(3,0)
         write(6,*) '*************************************************'
         write(6,*) 'Enter y for print Wave Components for Pitch'
         write(6,*) '      RETURN to skip'
         read(5,'(a)') yorn
**       yorn='n'
         if(yorn.eq.'y') then
            call lcolor(7,4)
            write(6,*) '      xi     etaC(xi)  etaS(xi)'
            do Ix=251,495,10
               xI=-10+0.02*(Ix-1)
               write(6,'(3f10.3)') xI,cEtax(Ix)
            enddo
         endif
* For alpha1-wave free condition
         call lcolor(2,0)
         write(6,*) '*************************************************'
         write(6,*) 'Solution for alpha-1 Wave Free'
*   Heave*heaveHa1+Pitch*pitchHa1=0
         Heave=(1,0)
         Pitch=-heaveHa1/pitchHa1*Heave
         Ha2=Heave*heaveHa2+Pitch*pitchHa2
         AHa2=abs(Ha2)
*   Modified to |Ha2|=1
         coef=1/AHa2
         Heave=Heave*coef
         Pitch=Pitch*coef
         Ha2  =Ha2  *coef
         AHa2=abs(Ha2)
*   Pressure
         do i=1,N
            p2(i)=p1(i)*coef+px(i)*Pitch
            p2C(i)=real(p2(i))
            p2S(i)=imag(p2(i))
            p(i)  =p2C(i)
            p(N+i)=p2S(i)
         enddo
         dEta2=dEta1*coef+dEtax*Pitch
         dEta2C=real(dEta2)
         dEta2S=imag(dEta2)
         p(N2p1)=dEta2C
         p(N2p2)=dEta2S
         call lcolor(3,0)
         write(6,*) '*************************************************'
         write(6,*) 'Enter y to print Pressure for alpha-1 wave free'
         write(6,*) '      RETURN to skip'
         read(5,'(a)') yorn
         if(yorn.eq.'y') then
            call lcolor(4,0)
            call vprt(N2,p,'Pressure Distribution : p2C,p2S(i)')
            write(6,'(a,2f10.3)') 'dEta2C,S =',dEta2C,dEta2S
         endif
*   Wave configuration
         do i=1,Mx
            cEta2(i)=cEta1(i)*coef+cEtax(i)*Pitch
         enddo
*             _______
         call AmpFunc(N,xsi,p,
*             ~~~~~~~
     *                Ha1,Ha2,
     *                AHa1,AHa2,PHa1,PHa2)
         call lcolor(7,5)
         write(6,*)      '*** Conditions for alpha-1 Wave Free ***'
         write(6,'(2(a,2f10.4))') 'Heave =',Heave,',  Pitch =',Pitch
         call lcolor(7,4)
         write(6,*) '*** Amplitude Functions for Alpha-1 Wave Free ***'
         write(6,*) '   Halpha1             Halpha2 '
         write(6,'(6f10.4)') Ha1,Ha2
         write(6,'(6f10.4)') AHa1,PHa1,AHa2,PHa2
         call lcolor(3,0)
         write(6,*) '*************************************************'
         write(6,*) 'Enter y for print Wave Components '//
     *              'for alpha-1 Wave Free'
         write(6,*) '      RETURN to skip'
         read(5,'(a)') yorn
         if(yorn.eq.'y') then
            call lcolor(7,4)
            write(6,*) '      xi     etaC(xi)  etaS(xi)'
            do Ix=251,495,10
               xI=-10+0.02*(Ix-1)
               write(6,'(3f10.3)') xI,cEta2(Ix)
            enddo
         endif
         goto 10
 20   continue
      call lcolor(0,0)
      end
************************************************************************
      subroutine ONtoKS(OmegaI,NuI,ALwm)
*
      common /Omega/Omega,Kappa,Nu,Sigma,Fn,U,somega,f
      real   Kappa,Nu,NuI
      pi=acos(0.0)*2
*
      Omega=OmegaI
      Nu=NuI
      Sigma=   Nu*Omega
      Kappa=Sigma*Omega
      Fn=1/sqrt(Nu)
      g=9.8
      U=sqrt(g*ALwm)*Fn
      somega=Sigma*U/ALwm
      f=2*pi/somega
      end
************************************************************************
      subroutine BeatAnl(PHa1,PHa2,WLBeat,xMax,xMin)
*
      common /WLen/WLena1,WLena2,WLenb1,WLenb2
*
      WLBeat=Wlena1*WLena2/(WLena2-WLena1)
**    xMax=-WLBeat*(PHa2-PHa1)/360
      xMax= WLBeat*(PHa2-PHa1)/360
 50   if(xMax.lt.-4) goto 60
         xMax=xMax-WLBeat
         goto 50
 60   continue
      xMin=xMax-WLBeat/2
      end
************************************************************************
      subroutine WaveCal(N,x,xsi,p,pEtac,pEtas,
     *                   Mx,xWave,cEta)
*      
*     To Calculate Wave Configuration (cEta) around a Hydro-Plane 
*
*
      complex cEta(*)
      real    xWave(*)
      real    x(*),xsi(*),p(*),pEtac(*),pEtas(*)
*
      M=496
      do Ix=1,M
         xI=-10+0.02*(Ix-1)
         call WaveHght(N,xI,Etac,Etas,xsi,p)
         xWave(Ix)=xI
         cEta(Ix)=cmplx(Etac,Etas)
      enddo 
      Ix=Ix-1
      do I=1,N
         xI=x(I)
         if(xI.le.5) then
            Ix=Ix+1
            xWave(Ix)=xI
            cEta(Ix)=cmplx(pEtac(I),pEtas(i))
         endif
      enddo
      Mx=Ix
      end
************************************************************************
      subroutine WaveHght(N,xI,Etac,Etas,xsi,p)
*
      common /ab12/alpha1,alpha2,beta1,beta2,sqop,csqom
      common /Omega/Omega,Kappa,Nu,Sigma,Fn,U,somega,f
*
      real    Kappa,Nu
      real    xsi(*),p(*)
      complex csqom,beta1,beta2
      complex zI,zetaJ,zetaF
      complex WGCfunc,WGC,WGS
      complex WQCfunc,WQC,WQS
      complex WmCfunc,WmC,WmS
      pi=acos(0.0)*2
* pC-pS-Part
      thetacut=pi/2
      coef=1/(2*pi*Nu)
      EtaC=0
      EtaS=0
      zI   =cmplx(xI,0)
      zetaJ=cmplx(xsi(1),0)
      WGC=WGCfunc(zI,zetaJ,thetacut,WGS)
      SGCJ=real(WGC)
      SGSJ=real(WGS)
      do J=1,N
         SGCJm1=SGCJ
         SGSJm1=SGSJ
         zetaJ=cmplx(xsi(J+1),0)
         WGC=WGCfunc(zI,zetaJ,thetacut,WGS)
         SGCJ=real(WGC)
         SGSJ=real(WGS)
         dSGCJ=  SGCJ-SGCJm1
         dSGSJ=  SGSJ-SGSJm1
         pCJ=p(  J)
         pSJ=p(N+J)
         EtaC=EtaC-coef*(pCJ*dSGCJ-pSJ*dSGSJ)
         EtaS=EtaS-coef*(pCJ*dSGSJ+pSJ*dSGCJ)
      enddo
* dEta-Part
      N2=N*2
      zetaF=xsi(N+1)
      dEtaC=p(N2+1)
      dEtaS=p(N2+2)
      WQC=WQCfunc(zI,zetaF,thetacut,WQS)
      SQC=real(WQC)
      SQS=real(WQS)
      WmC=WmCfunc(zI,zetaF,WmS)
      SmC=real(WmC)
      SmS=real(WmS)
      EtaC=EtaC+coef*(dEtaC*(-Sigma*SQS+SmC)
     *               +dEtaS*(-Sigma*SQC-SmS))
      EtaS=EtaS+coef*(dEtaC*( Sigma*SQC+SmS)
     *               +dEtaS*(-Sigma*SQS+SmC))
      end
************************************************************************
      subroutine PlateConf(N2D,N,Np1,N2p2,A,p,Etac,Etas)
*
      real A(N2D,*),p(*),Etac(*),Etas(*)
*
      do I=1,N
         Etac(I)=0
         Etas(I)=0
         do J=1,N2p2
            Etac(I)=Etac(I)+A(I,    J)*p(J)
            Etas(I)=Etas(I)+A(Np1+I,J)*p(J)
         enddo
      enddo
      end
************************************************************************
      subroutine CoefMat(N2D,N,x,xsi,A)
*
      common /ab12/alpha1,alpha2,beta1,beta2,sqop,csqom
      common /Omega/Omega,Kappa,Nu,Sigma,Fn,U,somega,f
      common /WLen/WLena1,WLena2,WLenb1,WLenb2
*
      real    Nu,Kappa
      real    A(N2D,*),x(*),xsi(*)
      complex csqom
      complex beta1,beta2
      complex zetaj,zi,zetaN
      complex WGCfunc,WGC,WGS
      complex WQCfunc,WQC,WQS
      complex WmCfunc,WmC,WmS
*
      pi=acos(0.0)*2
      thetacut=pi/2
      coef=1/(2*pi*Nu)
*
      do I=1,N2D
         do J=1,N2D
            A(I,J)=0
         enddo
      enddo
* Ai,j
      do I=1,N
         zi=cmplx(x(I),0)
         zetaj=cmplx(xsi(1),0)
         WGC=WGCfunc(zi,zetaj,thetacut,WGS)
         SGCj=real(WGC)
         SGSj=real(WGS)
         do J=1,N
            zetaj=cmplx(xsi(j+1),0)
            SGCjm1=SGCj
            SGSjm1=SGSj
            WGC=WGCfunc(zi,zetaj,thetacut,WGS)
            SGCj=real(WGC)
            SGSj=real(WGS)
            if(i.eq.j) then
               A(I,J) =-coef*(SGCj-SGCjm1)-1/Nu
            else
               A(I,J) =-coef*(SGCj-SGCjm1)
            endif
            A(I,N+J)  = coef*(SGSj-SGSjm1)
            A(N+I,J)  =-A(I,N+J)
            A(N+I,N+J)= A(I,J)
         enddo
      enddo
* for dEtaC, dEtaS
      N2=N*2
      zetaN=cmplx(xsi(N+1),0)
      do I=1,N
         zI=cmplx(x(I),0)
         WQC=WQCfunc(zI,zetaN,thetacut,WQS)
         WmC=WmCfunc(zI,zetaN,WmS)
         A(I,N2+1)  = coef*real(-Sigma*WQS+WmC)
         A(I,N2+2)  =-coef*real( Sigma*WQC+WmS)
         A(N+I,N2+1)=-A(I,N2+2)
         A(N+I,N2+2)= A(I,N2+1)
      enddo
* Kutta
      do J=1,N2+2
         A(N2+1,J)=0
         A(N2+2,J)=0
      enddo
      A(N2+1,1)  =-sqrt(x(2))
      A(N2+1,2)  = sqrt(x(1))
      A(N2+2,N+1)=-sqrt(x(2))
      A(N2+2,N+2)= sqrt(x(1))
      end
************************************************************************
      subroutine AmpFunc(N,xsi,p,
     *                   Ha1,Ha2,AHa1,AHa2,PHa1,PHa2)
*
      common /ab12/alpha1,alpha2,beta1,beta2,sqop,csqom
      common /Omega/Omega,Kappa,Nu,Sigma,Fn,U,somega,f
*
      real    Nu,Kappa
      real    xsi(*),p(*)
      complex Pcjs,dEtacjs
      complex Ha1,Ha2
      complex junit/(0,1)/
      complex csqom
      complex beta1,beta2
      complex Ea1K,  Ea2K
      complex Ea1Km1,Ea2Km1
*
      pi=acos(0.0)*2
      rd=180/pi
      N2=N*2
*
      coef1=1/(Nu*sqop)
*
* P^CjS
      Ha1=0
      Ha2=0
      xsiK=xsi(1)
      Ea1K=exp(-junit*alpha1*xsiK)
      Ea2K=exp(-junit*alpha2*xsiK)                 
      do K=1,N
         xsiK=xsi(K+1)
         Ea1Km1=Ea1K
         Ea2Km1=Ea2K
         Ea1K=exp(-junit*alpha1*xsiK)
         Ea2K=exp(-junit*alpha2*xsiK)                 
         Pcjs=cmplx(p(K),p(N+K))
         Ha1=Ha1+Pcjs*(Ea1K-Ea1Km1)
         Ha2=Ha2-Pcjs*(Ea2K-Ea2Km1)
      enddo
      Ha1= coef1*Ha1
      Ha2= coef1*Ha2
* dEta^CjS
      ama1=Sigma-alpha1
      ama2=Sigma-alpha2            
      xF=xsi(N+1)      
      dEtacjs=cmplx(p(N2+1),p(N2+2))
      Ha1=Ha1+coef1*dEtacjs*ama1*exp(-junit*alpha1*xF)
      Ha2=Ha2-coef1*dEtacjs*ama2*exp(-junit*alpha2*xF)
      AHa1=abs(Ha1)
      AHa2=abs(Ha2)
      PHa1=atan2(imag(Ha1),real(Ha1))*rd
      PHa2=atan2(imag(Ha2),real(Ha2))*rd
      end
************************************************************************
      subroutine YCoordnt(N,x,Eta1,Eta1c,Eta1s,Etax,EtaxC,EtaxS,ALd)
*
      real x(*),Eta1C(*),Eta1S(*),EtaxC(*),EtaxS(*)
      complex   Eta1(*),          Etax(*)
*
*     Giving y-coordinates eta(I) corresponding with x(I)
*
* For Heave(1)
      X0=(3-Ald)/2
      C0=2/(Ald-1)**3
      do I=1,N
         if(x(I).le.1) then
            Eta1C(I)=1
         elseif(x(I).le.Ald) then
            Eta1C(I)=C0*(x(I)-ALd)**2*(x(I)-X0)
         else
            Eta1C(I)=0
         endif
         Eta1S(I)=0
         Eta1(I)=cmplx(Eta1C(I),Eta1S(I))
      enddo
* For Pitch(x)
      X0=(1+Ald)/(2*ALd)
      C0=ALd/(ALd-1)**3
      do I=1,N
         if(x(I).le.1) then
            EtaxC(I)=x(I)-0.5
         elseif(x(I).le.Ald) then
            EtaxC(I)=C0*(x(I)-ALd)**2*(x(I)-X0)
         else
            EtaxC(I)=0
         endif
         EtaxS(I)=0
         Etax(I)=cmplx(EtaxC(I),EtaxS(I))
      enddo
      end
************************************************************************
      subroutine XCoordnt(N,x,xsi,ALf)
*
*     Creating x-coordinates : x midpoints between xsi(I) and xsi(I+1)
*
      real x(*),xsi(*)
      parameter ( a=2 )
*
      dZeta=(1-a/(ALf+a))/N
      do I=1,N+1
         ZetaI=1-(I-1)*dZeta
         xsi(I)=a/ZetaI-a
      enddo
      do I=1,N
         x(I)=(xsi(I)+xsi(I+1))/2
      enddo
      end
************************************************************************
      subroutine AsympWH(xI,etaIc,etaIs,alpha1,alpha2,Ha1,Ha2)
*
      complex Ha1,Ha2,eta,j/(0.0,1.0)/
*
      eta= Ha1*exp( j*alpha1*xI)
     *    +Ha2*exp( j*alpha2*xI)
      etaIc=eta
      etaIs=imag(eta)
      end
************************************************************************
      complex function WGCfunc(z,zeta,ThetaCut,WGS)
*
*       ThetaCut ( Angle of Cut of Log(z-zeta) ) must be POSITIVE
*
*      ThetaCut - 2*pi  <    Argument of Log(z-zeta)      =<  ThetaCut
*                      .lt.                              .le.
*             - 3/2 PI  < Argument of Log(z-zetaBar) & E1 =<  PI/2
* 
      common /ab12/alpha1,alpha2,beta1,beta2,sqop,csqom
      common /Omega/Omega,Kappa,Nu,Sigma,Fn,U,somega,f
*
      complex csqom,beta1,beta2
* 
      complex i/(0,1)/
      complex z,zeta,zetaBar,LogZ,LogZBar,WGS
      complex miza1,miza2,mizb1,mizb2
      complex  eia1, eia2, eib1, eib2
      complex eE1a1,eE1a2,eE1b1,eE1b2
      complex   Sa1,  Sa2,  Sb1,  Sb2
      real    Kappa,Nu
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
      miza1=-i*alpha1*(z-zetaBar)
      miza2=-i*alpha2*(z-zetaBar)
      mizb1=-i* beta1*(z-zetaBar)
      mizb2=-i* beta2*(z-zetaBar)
      eia1=exp(miza1)
      eia2=exp(miza2)
      eib1=exp(mizb1)
      eib2=exp(mizb2)
      call expi3(miza1,eE1a1)
      call expi3(miza2,eE1a2)
      call expi3(mizb1,eE1b1)
      call expi3(mizb2,eE1b2)
      xsigna =       real(z-zetaBar)
      xsignb1=real(beta1*(z-zetaBar))
      xsignb2=real(beta2*(z-zetaBar))
      if(Omega.lt.0.5) then
         if(xsigna.ge.0) then
            Sa1=eE1a1
            Sa2=eE1a2
         else
            Sa1=eE1a1+eia1*pi2*i
            Sa2=eE1a2+eia2*pi2*i
         endif
         if(xsignb1.ge.0) then
            Sb1=eE1b1
         else
            Sb1=eE1b1+eib1*pi2*i
         endif
         if(xsignb2.ge.0) then
            Sb2=eE1b2-eib2*pi2*i
         else
            Sb2=eE1b2
         endif
      else
         if(xsigna.ge.0) then
            Sa1=eE1a1
            Sa2=eE1a2
         else
            Sa1=eE1a1+eia1*pi2*i
            Sa2=eE1a2+eia2*pi2*i
         endif
         Sb1=eE1b1
         Sb2=eE1b2
      endif
      WGCfunc=-i*LogZ-i*LogZBar+i/sqop*(Sa1-Sa2)+i/csqom*(Sb1-Sb2)
      WGS=                     -1/sqop*(Sa1-Sa2)+1/csqom*(Sb1-Sb2)
      end
************************************************************************
      complex function WQCfunc(z,zeta,ThetaCut,WQS)
*
*       ThetaCut ( Angle of Cut of Log(z-zeta) ) must be POSITIVE
*
*      ThetaCut - 2*pi  <    Argument of Log(z-zeta)      =<  ThetaCut
*                      .lt.                              .le.
*             - 3/2 PI  < Argument of Log(z-zetaBar) & E1 =<  PI/2
*
      common /ab12/alpha1,alpha2,beta1,beta2,sqop,csqom
      common /Omega/Omega,kappa,nu,sigma,Fn,U,somega,f
      common /Sab12/Sa1,  Sa2,  Sb1,  Sb2
*
      complex csqom,beta1,beta2
* 
      complex i/(0,1)/
      complex z,zeta,zetaBar,LogZ,LogZBar,WQS
      complex miza1,miza2,mizb1,mizb2
      complex  eia1, eia2, eib1, eib2
      complex eE1a1,eE1a2,eE1b1,eE1b2
      complex   Sa1,  Sa2,  Sb1,  Sb2
      real    kappa,nu
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
      miza1=-i*alpha1*(z-zetaBar)
      miza2=-i*alpha2*(z-zetaBar)
      mizb1=-i* beta1*(z-zetaBar)
      mizb2=-i* beta2*(z-zetaBar)
      eia1=exp(miza1)
      eia2=exp(miza2)
      eib1=exp(mizb1)
      eib2=exp(mizb2)
      call expi3(miza1,eE1a1)
      call expi3(miza2,eE1a2)
      call expi3(mizb1,eE1b1)
      call expi3(mizb2,eE1b2)
      xsigna=real(z-zetaBar)
      if(xsigna.ge.0) then
         Sa1=eE1a1
         Sa2=eE1a2
      else
         Sa1=eE1a1+eia1*pi2*i
         Sa2=eE1a2+eia2*pi2*i
      endif
      if(Omega.lt.0.5) then
         xsignb1=real(beta1*(z-zetaBar))
         if(xsignb1.ge.0) then
            Sb1=eE1b1
         else
            Sb1=eE1b1+eib1*pi2*i
         endif
         xsignb2=real(beta2*(z-zetaBar))
         if(xsignb2.ge.0) then
            Sb2=eE1b2-eib2*pi2*i
         else
            Sb2=eE1b2
         endif
      else
         Sb1=eE1b1
         Sb2=eE1b2
      endif
      WQCfunc=LogZ-LogZBar+1/sqop*(Sa1-Sa2)+1/csqom*(Sb1-Sb2)
      WQS=                 i/sqop*(Sa1-Sa2)-i/csqom*(Sb1-Sb2)
      end
************************************************************************
      complex function WmCfunc(z,zeta,WmS)
*
      common /ab12/alpha1,alpha2,beta1,beta2,sqop,csqom
      common /Omega/Omega,kappa,nu,sigma,Fn,U,somega,f
      common /Sab12/Sa1,  Sa2,  Sb1,  Sb2
*
      complex csqom,beta1,beta2
* 
      complex i/(0,1)/
      complex z,zeta,zetaBar,InvZ,InvZBar,WmS
      complex miza1,miza2,mizb1,mizb2
      complex  eia1, eia2, eib1, eib2
      complex eE1a1,eE1a2,eE1b1,eE1b2
      complex   Sa1,  Sa2,  Sb1,  Sb2
      real    kappa,nu
*
      pi=acos(0.0)*2
      pi2=2*pi
*
      InvZ=1/(z-zeta)
      zetaBar=conjg(zeta)
      InvZBar=1/(z-zetaBar)
*
      miza1=-i*alpha1*(z-zetaBar)
      miza2=-i*alpha2*(z-zetaBar)
      mizb1=-i* beta1*(z-zetaBar)
      mizb2=-i* beta2*(z-zetaBar)
      eia1=exp(miza1)
      eia2=exp(miza2)
      eib1=exp(mizb1)
      eib2=exp(mizb2)
      call expi3(miza1,eE1a1)
      call expi3(miza2,eE1a2)
      call expi3(mizb1,eE1b1)
      call expi3(mizb2,eE1b2)
      xsigna =       real(z-zetaBar)
      xsignb1=real(beta1*(z-zetaBar))
      xsignb2=real(beta2*(z-zetaBar))
      if(Omega.le.0.5) then
         if(xsigna.ge.0) then
            Sa1=eE1a1
            Sa2=eE1a2
         else
            Sa1=eE1a1+eia1*pi2*i
            Sa2=eE1a2+eia2*pi2*i
         endif
         if(xsignb1.ge.0) then
            Sb1=eE1b1
         else
            Sb1=eE1b1+eib1*pi2*i
         endif
         if(xsignb2.ge.0) then
            Sb2=eE1b2-eib2*pi2*i
         else
            Sb2=eE1b2
         endif
      else
         if(xsigna.ge.0) then
            Sa1=eE1a1
            Sa2=eE1a2
         else
            Sa1=eE1a1+eia1*pi2*i
            Sa2=eE1a2+eia2*pi2*i
         endif
         Sb1=eE1b1
         Sb2=eE1b2
      endif
      WmCfunc=-InvZ+InvZBar+i/sqop *(alpha1*Sa1-alpha2*Sa2)
     *                     +i/csqom*( beta1*Sb1- beta2*Sb2)
      WmS=                 -1/sqop *(alpha1*Sa1-alpha2*Sa2)
     *                     +1/csqom*( beta1*Sb1- beta2*Sb2)
      end
************************************************************************
      subroutine ab12etc
*
      common /ab12/alpha1,alpha2,beta1,beta2,sqop,csqom
      common /Omega/Omega,Kappa,Nu,Sigma,Fn,U,somega,f
      common /WLen/WLena1,WLena2,WLenb1,WLenb2
*
      complex csqom,beta1,beta2,i/(0.0,1.0)/
      real    Kappa,Nu
      real    minOmega/0.3e-3/
      pi=acos(0.0)*2
      pi2=pi*2
*
      if(Omega.eq.0.25) then
         write(6,*) 'Omega = 0.25 occured STOP by sub. ab12etc'
         stop
      endif
      Omega4=4*Omega
      Omega2=2*Omega
      sqop=sqrt(    1+Omega4)
      sqom=sqrt(abs(1-Omega4))
      alpha1=nu/2*(1+Omega2+sqop)
      if(Omega.ge.minOmega) then
         alpha2=nu/2*(1+Omega2-sqop)
      else
         alpha2=Kappa
         call lcolor(7,2)
         write(6,*) 'Omega < minOmega happens from sub. ab12etc'
         call lcolor(0,0)
      endif
      WLena1=pi2*Fn**2*2/(1+Omega2+sqop)
      WLena2=pi2/alpha2
      if(Omega4.le.1) then
         csqom=sqom
         beta1=nu/2*(1-Omega2+sqom)
         if(Omega.ge.minOmega) then
            beta2=nu/2*(1-Omega2-sqom)
         else
            beta2=kappa
         endif
         WLenb1=pi2*Fn**2*2/(1-Omega2+sqom)
         WLenb2=pi2/beta2
      else
         csqom=i*sqom
         beta1=nu/2*(1-Omega2+i*sqom)
         beta2=nu/2*(1-Omega2-i*sqom)
         WLenb1=0
         WLenb2=0
      endif
      end
************************************************************************
      SUBROUTINE VPRT(M,V,TITLE)                                        
*                                                                       
*     VECTOR PRINT OUT in 10-colum type
*                                                                       
      REAL      V(*)
      CHARACTER TITLE*(*)                                               
*                                                                       
      WRITE(6,100) '*** ',TITLE,' ***'         
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
  100 FORMAT (/3A)                                                 
  110 FORMAT(8X,5(I3,4X),2X,5(I3,4X))
  120 FORMAT(I4,2X,5F7.3,2X,5F7.3)                                      
      END                                                               
************************************************************************
      SUBROUTINE APRT1(MD,M,N,A,TITLE)                                  
*                                                                       
*     ARRAY PRINT OUT in 5-colum type
*                                                                       
      REAL          A(MD,*)                                  
      CHARACTER*(*) TITLE                                               
*                                                                       
      J2=0
   10 CONTINUE                                                          
        IF(J2.NE.N) THEN                                                
        J1=J2+1                                                         
        J2=MIN(J1+4,N)                                                  
        I2=0
   20   CONTINUE                                                        
          IF(I2.NE.M) THEN                                              
          I1=I2+1                                                       
          I2=MIN(I1+49,M)                                               
          WRITE (6,100) '*** ',TITLE,' ***'                    
          WRITE (6,110) (J,J=J1,J2)                                     
          DO 30 I=I1,I2                                                 
            WRITE (6,120) I,(A(I,J),J=J1,J2)                           
   30     CONTINUE                                                      
          GO TO 20                                                      
        ENDIF                                                           
        GOTO 10                                                         
      ENDIF                                                             
  100 FORMAT (/3A)                                                  
  110 FORMAT(5X,5(4X,I3,7X))                                           
  120 FORMAT(I3,2X,5f14.5)                                              
      END
************************************************************************
      SUBROUTINE APRT(MD,M,N,A,TITLE)                                   
*                                                                       
*     ARRAY PRINT OUT in 10-colum type
*                                                                       
      REAL A(MD,*)
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
          WRITE (6,100) '*** ',TITLE,' ***'                     
          WRITE (6,110) (J,J=J1,J2)                                     
          DO 30 I=I1,I2                                                 
          WRITE (6,120) I,(A(I,J),J=J1,J2)                            
   30     CONTINUE                                                      
          GO TO 20                                                      
        ENDIF                                                           
        GOTO 10                                                         
      ENDIF                                                             
  100 FORMAT(/3A)                                           
  110 FORMAT(8X,5(I3,4X),2X,5(I3,4X))                                 
**120 FORMAT(I4,2X,5f7.2,2X,5f7.2)                                      
  120 FORMAT(I4,2X,5f7.3,2X,5f7.3)                                      
      END                                                               
************************************************************************
      SUBROUTINE    EXPI3 (Z,EXPE1)
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
*********************************************************************** 
**    SUBROUTINE    ExpInt(Z,E1)
      SUBROUTINE    ExpInt(sZ,sE1)
*
*     EXPONENTIAL INTEGRAL OF COMPLEX ARGUMENT
*     CODED BY KATSUO SUZUKI (BODAI)
*
      IMPLICIT  COMPLEX*16  (Z)
      implicit real*8 (a-h,o-y)
      complex*8 sZ,sE1
      REAL*8 INF/9.99999999999999D09/
      COMPLEX*16  E1,E1GL,EXPE1,LOGZ
      REAL*8 GAMMA/0.5772156649D00/
      REAL*8   PAI/3.14159265359D0/
**    RETURN
*
**    ENTRY  EXPI1 (Z,E1)
**    ENTRY  EXPI2 (Z,E1GL)
**    ENTRY  EXPI3 (Z,EXPE1)
**    ENTRY  EXPI4 (Z,ZEXPE1)
**    ENTRY  EXPIAL(Z,E1,E1GL,EXPE1,ZEXPE1)
*
*          E1 =COMPLEX EXPONENTIAL INTEGRAL OF COMPLEX ARGUMENT Z
*        E1GL =E1 + GAMMA + LOG( Z )
*       EXPE1 = EXP( Z ) * E1
*      ZEXPE1 = Z * EXPE1
*
      Z=sZ
      R=ABS(Z)
      X=real(Z)
      Y=dIMAG(Z)
      IF(R.EQ.0)   GO TO 10
      LOGZ=LOG(Z)
      IF(R.GT.25)  GO TO 40
      IF(R.GT.4.AND.X.GE.0)  GO TO 30
      IF(ABS(Y).GT.4)  GO TO 30
      GO TO 20
*
*         R = 0
*
   10 CONTINUE
      E1=DCMPLX(INF,0d0)
      E1GL=(1d0,0d0)
      EXPE1=E1
      ZEXPE1=DCMPLX(GAMMA,0d0)
      WRITE(6,100)
  100 FORMAT('   *** (EXPINT)  Z=(0.0,0.0)  ***')
      sE1=E1
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
         AD=ABS(ZI)*1d8
      IF(RE.LE.AD)  GO TO 21
      E1GL=ZSUM
      E1=E1GL-GAMMA-LOGZ
      EXPE1=EXP(Z)*E1
      ZEXPE1=Z*EXPE1
      sE1=E1
      RETURN
*
*         CONTINUED  FRACTION
*
*              EXPE1 = 1/Z+1/1+1/Z+2/1+2/Z+3/1+3/Z+
*
   30 CONTINUE
      I=11
      Z0=(0d0,0d0)
      ZI=Z0
   31 IF(I.EQ.1) GO TO 35
         I=I-1
         AI=DFLOAT(I)
         ZD=Z+ZI
         IF(ZD.NE.0) GO TO 32
            ZI=Z0
         GO TO 33
   32       ZI=AI/ZD
   33    CONTINUE
         ZD=1.0+ZI
         IF(ZD.NE.0) GO TO 34
            ZI=Z0
            GO TO 31
   34    CONTINUE
         ZI=AI/ZD
         GO TO 31
   35 CONTINUE
      EXPE1=1/(Z+ZI)
      E1=EXP(-Z)*EXPE1
      E1GL=E1+GAMMA+LOGZ
      ZEXPE1=Z*EXPE1
      sE1=E1
      RETURN
*
*         ASYMPTOTIC EXPANSION
*
*              ZEXPE1 = 1-1/Z+FACT(2)/Z**2-FACT(3)/Z**3+
*
   40 CONTINUE
      ZINV=1/Z
      I=0
      ZI=(1d0,0d0)
      ZSUM=ZI
   41 I=I+1
         AI=DFLOAT(I)
         ZI=-AI*ZINV*ZI
         ZSUM=ZSUM+ZI
         RE=ABS(ZSUM)
         AD=ABS(ZI)*1d8
      IF(RE.LE.AD)  GO TO 41
      IF(Y.EQ.0.AND.X.LT.0)  ZSUM=ZSUM-Z*EXP(Z)*DCMPLX(0d0,PAI)
      ZEXPE1=ZSUM
      EXPE1=ZEXPE1*ZINV
      IF(-X.GE.200) GO TO 42
         E1=EXP(-Z)*EXPE1
         E1GL=E1+GAMMA+LOGZ
         sE1=E1
         RETURN
   42 E1=INF*EXP(DCMPLX(0d0,-Y))*EXPE1
      E1GL=E1+GAMMA+LOGZ
      sE1=E1
      RETURN
      END
************************************************************************
      SUBROUTINE SOLVE(MD,MT,M1,A,U,V,W,G,R,Z,S,ES,PFLG,EPS)            
*                                                                       
*     TO SOLVE A*S=G BY USE OF SVD METHOD   A=A(MT*M1)                  
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
      IF(PFLG) then
**       call lcolor(5,4)
**      CALL APRT(MD,M1,M1,V,'V(I,J)  ') 
      endif                               
* 
      call lcolor(2,0)
      WRITE(6,110) IERR
      if(pflg) then
         call lcolor(5,4)
         CALL VPRT(M1,W,'W(I)    ')   
      endif                                     
*                                                                       
*     ***  GIVE RHS, G, ONLY                                            
*   
      ENTRY SOLVE1(MD,MT,M1,  U,V,W,G,R,Z,S,ES,PFLG,EPS) 
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
         call lcolor(5,4)
         CALL VPRT(M1,R,'R(I)    ')  
      endif                                      
*                                                                       
*     SLUTION FOR  W*Z=R                                                
*     CHECK FOR EIGEN SOLUTION                                          
*                                                                       
      DO 40 I=1,M1                                                      
        Z(I)=0.0                                                        
        IF(W(I).LE.EPS) GO TO 43                                        
          Z(I)=R(I)/W(I)                                                
          GO TO 40                                                      
   43   CONTINUE                                                        
        DO 45 J=1,M1                                                    
          ES(J)=V(J,I)                                                  
   45   CONTINUE                                                        
        WRITE (6,120) I                                                 
        CALL VPRT(M1,ES,'ES(I)   ')                                     
   40 CONTINUE                                                          
*                                                                       
*     SOLUTINO FOR V*S=Z                                                
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
  110 FORMAT(5X,'IERR =',I4,'   from SVD') 
  120 FORMAT(5X,I5,'-TH  IS  AN EIGEN VECTOR')                        
      END                                                               
************************************************************************
      SUBROUTINE SVD(NM,M,N,A,W,MATU,U,MATV,V,IERR,RV1)                 
*                                                                       
      INTEGER I,J,K,L,M,N,II,I1,KK,K1,LL,L1,MN,NM,ITS,IERR              
      REAL A(NM,N),W(N),U(NM,N),V(NM,N),RV1(N)                          
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

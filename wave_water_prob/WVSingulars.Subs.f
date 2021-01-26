* This file contains the followings
*
***  ab12etc
***  WQCfunc, WmCfunc,  VmCfunc,  dVmCfunc
***  WGCfunc, WmuCfunc, VmuCfunc, dVmuCfunc
***  VLog, LogNK
***  WQintCfunc, VQintCfunc, dVQintCfunc
***  EXPI3
***                                 Fixed on 2017/04
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
         call pausebeep
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
      complex function VmCfunc(z,zeta,VmS)
*
      common /ab12/alpha1,alpha2,beta1,beta2,sqop,csqom
      common /Omega/Omega,kappa,nu,sigma,Fn,U,somega,f
      common /Sab12/Sa1,  Sa2,  Sb1,  Sb2
*
      complex csqom,beta1,beta2
* 
      complex i/(0,1)/
      complex z,zeta,zetaBar,InvZ,InvZBar,VmS
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
      VmCfunc=InvZ**2-InvZBar**2
     *  +1/sqop *(alpha1**2*Sa1-alpha2**2*Sa2-i*(alpha1-alpha2)*InvZBar)
     *  +1/csqom*( beta1**2*Sb1- beta2**2*Sb2-i*( beta1- beta2)*InvZBar)
      VmS=
     *  +i/sqop *(alpha1**2*Sa1-alpha2**2*Sa2-i*(alpha1-alpha2)*InvZBar)
     *  -i/csqom*( beta1**2*Sb1- beta2**2*Sb2-i*( beta1- beta2)*InvZBar)
      end
************************************************************************
      complex function dVmCfunc(z,zeta,dVmS)
*
      common /ab12/alpha1,alpha2,beta1,beta2,sqop,csqom
      common /Omega/Omega,kappa,nu,sigma,Fn,U,somega,f
      common /Sab12/Sa1,  Sa2,  Sb1,  Sb2
*
      complex csqom,beta1,beta2
* 
      complex i/(0,1)/
      complex z,zeta,zetaBar,InvZ,InvZBar,dVmS
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
      dVmCfunc=-2*InvZ**3+2*InvZBar**3
     *  -i/sqop *(alpha1**3*Sa1-alpha2**3*Sa2
     *      -(alpha1-alpha2)*InvZBar**2-i*(alpha1**2-alpha2**2)*InvZBar)
     *  -i/csqom*( beta1**3*Sb1- beta2**3*Sb2
     *      -( beta1- beta2)*InvZBar**2-i*( beta1**2- beta2**2)*InvZBar)
      dVmS=
     *  +1/sqop *(alpha1**3*Sa1-alpha2**3*Sa2
     *      -(alpha1-alpha2)*InvZBar**2-i*(alpha1**2-alpha2**2)*InvZBar)
     *  -1/csqom*( beta1**3*Sb1- beta2**3*Sb2
     *      -( beta1- beta2)*InvZBar**2-i*( beta1**2- beta2**2)*InvZBar)
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
      complex function WmuCfunc(z,zeta,WmuS)
*
      common /ab12/alpha1,alpha2,beta1,beta2,sqop,csqom
      common /Omega/Omega,kappa,nu,sigma,Fn,U,somega,f
      common /Sab12/Sa1,  Sa2,  Sb1,  Sb2
*
      complex csqom,beta1,beta2
* 
      complex i/(0,1)/
      complex z,zeta,zetaBar,InvZ,InvZBar,WmuS
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
      WmuCfunc=i*InvZ+i*InvZBar-1/sqop *(alpha1*Sa1-alpha2*Sa2)
     *                         -1/csqom*( beta1*Sb1- beta2*Sb2)
      WmuS=                    -i/sqop *(alpha1*Sa1-alpha2*Sa2)
     *                         +i/csqom*( beta1*Sb1- beta2*Sb2)
      end
************************************************************************
      complex function VmuCfunc(z,zeta,VmuS)
*
      common /ab12/alpha1,alpha2,beta1,beta2,sqop,csqom
      common /Omega/Omega,kappa,nu,sigma,Fn,U,somega,f
      common /Sab12/Sa1,  Sa2,  Sb1,  Sb2
*
      complex csqom,beta1,beta2
* 
      complex i/(0,1)/
      complex z,zeta,zetaBar,InvZ,InvZBar,VmuS
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
      VmuCfunc=-i*InvZ**2-i*InvZBar**2
     *  +i/sqop *(alpha1**2*Sa1-alpha2**2*Sa2-i*(alpha1-alpha2)*InvZBar)
     *  +i/csqom*( beta1**2*Sb1- beta2**2*Sb2-i*( beta1- beta2)*InvZBar)
      VmuS
     * =-1/sqop *(alpha1**2*Sa1-alpha2**2*Sa2-i*(alpha1-alpha2)*InvZBar)
     *  +1/csqom*( beta1**2*Sb1- beta2**2*Sb2-i*( beta1- beta2)*InvZBar)
      end
************************************************************************
      complex function dVmuCfunc(z,zeta,dVmuS)
*
*
      common /ab12/alpha1,alpha2,beta1,beta2,sqop,csqom
      common /Omega/Omega,kappa,nu,sigma,Fn,U,somega,f
      common /Sab12/Sa1,  Sa2,  Sb1,  Sb2
*
      complex csqom,beta1,beta2
* 
      complex i/(0,1)/
      complex z,zeta,zetaBar,InvZ,InvZBar,dVmuS
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
      dVmuCfunc=2*i*InvZ**3+2*i*InvZBar**3
     *  +1/sqop *(alpha1**3*Sa1-alpha2**3*Sa2
     *      -(alpha1-alpha2)*InvZBar**2-i*(alpha1**2-alpha2**2)*InvZBar)
     *  +1/csqom*( beta1**3*Sb1- beta2**3*Sb2
     *      -( beta1- beta2)*InvZBar**2-i*( beta1**2- beta2**2)*InvZBar)
      dVmuS=
     *  +i/sqop *(alpha1**3*Sa1-alpha2**3*Sa2
     *      -(alpha1-alpha2)*InvZBar**2-i*(alpha1**2-alpha2**2)*InvZBar)
     *  -i/csqom*( beta1**3*Sb1- beta2**3*Sb2
     *      -( beta1- beta2)*InvZBar**2-i*( beta1**2- beta2**2)*InvZBar)
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
      complex function WQintCfunc(z,zeta2,zeta1,zetaM,WQintS)
*                      WQintWB_C,S
*                      WQintNK_C,S
*     
*     zeta1, zeta2 are exchanegable
*
*     Cut of log(z-zeta) is set as
*        zeta1 -- zetaM -- zeta2
*
*     Cut of log(z-zetaBar) and E1 as
*        zetaBar -- (xsi,inf)
*
      common /ab12/alpha1,alpha2,beta1,beta2,sqop,csqom
      common /Omega/Omega,kappa,nu,sigma,Fn,U,somega,f
      common /Sab12/Sa1,  Sa2,  Sb1,  Sb2
      complex csqom,beta1,beta2
*
      complex i/(0,1)/
      complex WQintC1,WQintC2
      complex WQintS1,WQintS2,WQintS
      complex z,zeta1,zeta2,zetaM
      complex zdif,zdifBar,dzeta
      complex LogNK,VLog
      complex LogZ,LogZBar
      complex EiG,EigBar
* 
      complex miza1,miza2,mizb1,mizb2
      complex  eia1, eia2, eib1, eib2
      complex eE1a1,eE1a2,eE1b1,eE1b2
      complex   Sa1,  Sa2,  Sb1,  Sb2
      real    kappa,nu
*
      pi=acos(0.0)*2
      pi2=2*pi
*
      dzeta=zeta2-zeta1
      EiG=dzeta/abs(dzeta)
      EiGBar=conjg(EiG)
*
*     For zeta2
*
      zdif   =z-zeta2
      zdifBar=z-conjg(zeta2)
      LogZ=LogNK(z,zeta2,zetaM)
**    LogZ=VLog(zdif)
      LogZBar=VLog(zdifBar)
*
      miza1=-i*alpha1*zdifBar
      miza2=-i*alpha2*zdifBar
      mizb1=-i* beta1*zdifBar
      mizb2=-i* beta2*zdifBar
      eia1=exp(miza1)
      eia2=exp(miza2)
      eib1=exp(mizb1)
      eib2=exp(mizb2)
      call expi3(miza1,eE1a1)
      call expi3(miza2,eE1a2)
      call expi3(mizb1,eE1b1)
      call expi3(mizb2,eE1b2)
      xsigna=real(zdifBar)
      if(xsigna.ge.0) then
         Sa1=eE1a1
         Sa2=eE1a2
      else
         Sa1=eE1a1+eia1*pi2*i
         Sa2=eE1a2+eia2*pi2*i
      endif
      if(Omega.lt.0.5) then
         xsignb1=real(beta1*zdifBar)
         if(xsignb1.ge.0) then
            Sb1=eE1b1
         else
            Sb1=eE1b1+eib1*pi2*i
         endif
         xsignb2=real(beta2*zdifBar)
         if(xsignb2.ge.0) then
            Sb2=eE1b2-eib2*pi2*i
         else
            Sb2=eE1b2
         endif
      else
         Sb1=eE1b1
         Sb2=eE1b2
      endif
      WQintC2=-EiGBar*zdif   *(LogZ-1)
     *        +EiG   *zdifBar*(LogzBar-1)
     *        +EiG*2*i/(nu*Omega**2)*LogzBar
     *        -EiG*i/sqop *(Sa1/alpha1-Sa2/alpha2)
     *        -EiG*i/csqom*(Sb1/ beta1-Sb2/ beta2)
      WQintS2= EiG  /sqop *(Sa1/alpha1-Sa2/alpha2)
     *        -EiG  /csqom*(Sb1/ beta1-Sb2/ beta2)
*
*     For zeta1
*
      zdif   =z-zeta1
      zdifBar=z-conjg(zeta1)
      LogZ=LogNK(z,zeta1,zetaM)
**    LogZ=VLog(zdif)
**    LogZ=LogNK(z,zeta1,zeta2)
      LogZBar=VLog(zdifBar)
*
      miza1=-i*alpha1*zdifBar
      miza2=-i*alpha2*zdifBar
      mizb1=-i* beta1*zdifBar
      mizb2=-i* beta2*zdifBar
      eia1=exp(miza1)
      eia2=exp(miza2)
      eib1=exp(mizb1)
      eib2=exp(mizb2)
      call expi3(miza1,eE1a1)
      call expi3(miza2,eE1a2)
      call expi3(mizb1,eE1b1)
      call expi3(mizb2,eE1b2)
      xsigna=real(zdifBar)
      if(xsigna.ge.0) then
         Sa1=eE1a1
         Sa2=eE1a2
      else
         Sa1=eE1a1+eia1*pi2*i
         Sa2=eE1a2+eia2*pi2*i
      endif
      if(Omega.lt.0.5) then
         xsignb1=real(beta1*zdifBar)
         if(xsignb1.ge.0) then
            Sb1=eE1b1
         else
            Sb1=eE1b1+eib1*pi2*i
         endif
         xsignb2=real(beta2*zdifBar)
         if(xsignb2.ge.0) then
            Sb2=eE1b2-eib2*pi2*i
         else
            Sb2=eE1b2
         endif
      else
         Sb1=eE1b1
         Sb2=eE1b2
      endif
      WQintC1=-EiGBar*zdif   *(LogZ-1)
     *        +EiG   *zdifBar*(LogzBar-1)
     *        +EiG*2*i/(nu*Omega**2)*LogzBar
     *        -EiG*i/sqop *(Sa1/alpha1-Sa2/alpha2)
     *        -EiG*i/csqom*(Sb1/ beta1-Sb2/ beta2)
      WQintS1= EiG  /sqop *(Sa1/alpha1-Sa2/alpha2)
     *        -EiG  /csqom*(Sb1/ beta1-Sb2/ beta2)
*
      WQintCfunc=WQintC2-WQintC1
      WQintS    =WQintS2-WQintS1
      end
************************************************************************
      complex function VQintCfunc(z,zeta2,zeta1,zetaM,VQintS)
*                      VQintWB_C,S
*                      VQintNK_C,S
*     
*     zeta1, zeta2 are exchangeable
*
*     Cut of log(z-zeta) is set as
*        zeta1 -- zetaM -- zeta2
*
*     Cut of log(z-zetaBar) and E1 as
*        zetaBar -- (xsi,inf)
*
      common /ab12/alpha1,alpha2,beta1,beta2,sqop,csqom
      common /Omega/Omega,kappa,nu,sigma,Fn,U,somega,f
      common /Sab12/Sa1,  Sa2,  Sb1,  Sb2
      complex csqom,beta1,beta2
*
      complex i/(0,1)/
      complex VQintC1,VQintC2
      complex VQintS1,VQintS2,VQintS
      complex z,zeta1,zeta2,zetaM
      complex zdif,zdifBar,dzeta
      complex LogNK,VLog
      complex LogZ,LogZBar
      complex EiG,EigBar
* 
      complex miza1,miza2,mizb1,mizb2
      complex  eia1, eia2, eib1, eib2
      complex eE1a1,eE1a2,eE1b1,eE1b2
      complex   Sa1,  Sa2,  Sb1,  Sb2
      real    kappa,nu
*
      pi=acos(0.0)*2
      pi2=2*pi
*
      dzeta=zeta2-zeta1
      EiG=dzeta/abs(dzeta)
      EiGBar=conjg(EiG)
*
*     For zeta2
*
      LogZ=LogNK(z,zeta2,zetaM)
**    LogZ=VLog(z-zeta2)
      zdif   =z-zeta2
      zdifBar=z-conjg(zeta2)
      LogZBar=VLog(zdifBar)
      LogZ=log(zdif)
*
      miza1=-i*alpha1*zdifBar
      miza2=-i*alpha2*zdifBar
      mizb1=-i* beta1*zdifBar
      mizb2=-i* beta2*zdifBar
      eia1=exp(miza1)
      eia2=exp(miza2)
      eib1=exp(mizb1)
      eib2=exp(mizb2)
      call expi3(miza1,eE1a1)
      call expi3(miza2,eE1a2)
      call expi3(mizb1,eE1b1)
      call expi3(mizb2,eE1b2)
      xsigna=real(zdifBar)
      if(xsigna.ge.0) then
         Sa1=eE1a1
         Sa2=eE1a2
      else
         Sa1=eE1a1+eia1*pi2*i
         Sa2=eE1a2+eia2*pi2*i
      endif
      if(Omega.lt.0.5) then
         xsignb1=real(beta1*zdifBar)
         if(xsignb1.ge.0) then
            Sb1=eE1b1
         else
            Sb1=eE1b1+eib1*pi2*i
         endif
         xsignb2=real(beta2*zdifBar)
         if(xsignb2.ge.0) then
            Sb2=eE1b2-eib2*pi2*i
         else
            Sb2=eE1b2
         endif
      else
         Sb1=eE1b1
         Sb2=eE1b2
      endif
      VQintC2=-EiGBar*(LogZ-1)
     *        +EiG   *(LogzBar-1)
     *        -EiG/sqop *(Sa1-Sa2)
     *        -EiG/csqom*(Sb1-Sb2)
      VQintS2=-EiG*i/sqop *(Sa1-Sa2)
     *        +EiG*i/csqom*(Sb1-Sb2)
*
*     For zeta1
*
      LogZ=LogNK(z,zeta1,zetaM)
**    LogZ=VLog(z-zeta1)
      zdif   =z-zeta1
      zdifBar=z-conjg(zeta1)
      LogZBar=VLog(zdifBar)
      LogZ=log(zdif)
*
      miza1=-i*alpha1*zdifBar
      miza2=-i*alpha2*zdifBar
      mizb1=-i* beta1*zdifBar
      mizb2=-i* beta2*zdifBar
      eia1=exp(miza1)
      eia2=exp(miza2)
      eib1=exp(mizb1)
      eib2=exp(mizb2)
      call expi3(miza1,eE1a1)
      call expi3(miza2,eE1a2)
      call expi3(mizb1,eE1b1)
      call expi3(mizb2,eE1b2)
      xsigna=real(zdifBar)
      if(xsigna.ge.0) then
         Sa1=eE1a1
         Sa2=eE1a2
      else
         Sa1=eE1a1+eia1*pi2*i
         Sa2=eE1a2+eia2*pi2*i
      endif
      if(Omega.lt.0.5) then
         xsignb1=real(beta1*zdifBar)
         if(xsignb1.ge.0) then
            Sb1=eE1b1
         else
            Sb1=eE1b1+eib1*pi2*i
         endif
         xsignb2=real(beta2*zdifBar)
         if(xsignb2.ge.0) then
            Sb2=eE1b2-eib2*pi2*i
         else
            Sb2=eE1b2
         endif
      else
         Sb1=eE1b1
         Sb2=eE1b2
      endif
      VQintC1=-EiGBar*(LogZ-1)
     *        +EiG   *(LogzBar-1)
     *        -EiG/sqop *(Sa1-Sa2)
     *        -EiG/csqom*(Sb1-Sb2)
      VQintS1=-EiG*i/sqop *(Sa1-Sa2)
     *        +EiG*i/csqom*(Sb1-Sb2)
*
      VQintCfunc=VQintC2-VQintC1
      VQintS    =VQintS2-VQintS1
      end
************************************************************************
      complex function dVQintCfunc(z,zeta2,zeta1,dVQintS)
*     
*     zeta1, zeta2 are exchangeable 
*
*     Cut of log(z-zeta) is set as
*        zeta1 -- zetaM -- zeta2
*
*     Cut of log(z-zetaBar) and E1 as
*        zetaBar -- (xsi,inf)
*
      common /ab12/alpha1,alpha2,beta1,beta2,sqop,csqom
      common /Omega/Omega,kappa,nu,sigma,Fn,U,somega,f
      common /Sab12/Sa1,  Sa2,  Sb1,  Sb2
      complex csqom,beta1,beta2
*
      complex i/(0,1)/
      complex dVQintC1,dVQintC2
      complex dVQintS1,dVQintS2,dVQintS
      complex z,zeta1,zeta2
      complex zdif,zdifBar,dzeta
      complex EiG,EigBar
* 
      complex miza1,miza2,mizb1,mizb2
      complex  eia1, eia2, eib1, eib2
      complex eE1a1,eE1a2,eE1b1,eE1b2
      complex   Sa1,  Sa2,  Sb1,  Sb2
      real    kappa,nu
*
      pi=acos(0.0)*2
      pi2=2*pi
*
      dzeta=zeta2-zeta1
      EiG=dzeta/abs(dzeta)
      EiGBar=conjg(EiG)
*
*     For zeta2
*
      zdif   =z-zeta2
      zdifBar=z-conjg(zeta2)
*
      miza1=-i*alpha1*zdifBar
      miza2=-i*alpha2*zdifBar
      mizb1=-i* beta1*zdifBar
      mizb2=-i* beta2*zdifBar
      eia1=exp(miza1)
      eia2=exp(miza2)
      eib1=exp(mizb1)
      eib2=exp(mizb2)
      call expi3(miza1,eE1a1)
      call expi3(miza2,eE1a2)
      call expi3(mizb1,eE1b1)
      call expi3(mizb2,eE1b2)
      xsigna=real(zdifBar)
      if(xsigna.ge.0) then
         Sa1=eE1a1
         Sa2=eE1a2
      else
         Sa1=eE1a1+eia1*pi2*i
         Sa2=eE1a2+eia2*pi2*i
      endif
      if(Omega.lt.0.5) then
         xsignb1=real(beta1*zdifBar)
         if(xsignb1.ge.0) then
            Sb1=eE1b1
         else
            Sb1=eE1b1+eib1*pi2*i
         endif
         xsignb2=real(beta2*zdifBar)
         if(xsignb2.ge.0) then
            Sb2=eE1b2-eib2*pi2*i
         else
            Sb2=eE1b2
         endif
      else
         Sb1=eE1b1
         Sb2=eE1b2
      endif
      dVQintC2=-EiGBar/zdif
     *         +EiG   /zdifBar
     *         +EiG*i/sqop *(alpha1*Sa1-alpha2*Sa2)
     *         +EiG*i/csqom*(beta1 *Sb1- beta2*Sb2)
      dVQintS2=-EiG/sqop *(alpha1*Sa1-alpha2*Sa2)
     *         +EiG/csqom*( beta1*Sb1 -beta2*Sb2)
*
*     For zeta1
*
      zdif   =z-zeta1
      zdifBar=z-conjg(zeta1)
*
      miza1=-i*alpha1*zdifBar
      miza2=-i*alpha2*zdifBar
      mizb1=-i* beta1*zdifBar
      mizb2=-i* beta2*zdifBar
      eia1=exp(miza1)
      eia2=exp(miza2)
      eib1=exp(mizb1)
      eib2=exp(mizb2)
      call expi3(miza1,eE1a1)
      call expi3(miza2,eE1a2)
      call expi3(mizb1,eE1b1)
      call expi3(mizb2,eE1b2)
      xsigna=real(zdifBar)
      if(xsigna.ge.0) then
         Sa1=eE1a1
         Sa2=eE1a2
      else
         Sa1=eE1a1+eia1*pi2*i
         Sa2=eE1a2+eia2*pi2*i
      endif
      if(Omega.lt.0.5) then
         xsignb1=real(beta1*zdifBar)
         if(xsignb1.ge.0) then
            Sb1=eE1b1
         else
            Sb1=eE1b1+eib1*pi2*i
         endif
         xsignb2=real(beta2*zdifBar)
         if(xsignb2.ge.0) then
            Sb2=eE1b2-eib2*pi2*i
         else
            Sb2=eE1b2
         endif
      else
         Sb1=eE1b1
         Sb2=eE1b2
      endif
      dVQintC1=-EiGBar/zdif
     *         +EiG   /zdifBar
     *         +EiG*i/sqop *(alpha1*Sa1-alpha2*Sa2)
     *         +EiG*i/csqom*(beta1 *Sb1- beta2*Sb2)
      dVQintS1=-EiG/sqop *(alpha1*Sa1-alpha2*Sa2)
     *         +EiG/csqom*( beta1*Sb1 -beta2*Sb2)
*
      dVQintCfunc=dVQintC2-dVQintC1
      dVQintS    =dVQintS2-dVQintS1
      end


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




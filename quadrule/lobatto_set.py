#! /usr/bin/env python
#
def lobatto_set ( n ):

#*****************************************************************************80
#
## LOBATTO_SET sets abscissas and weights for Lobatto quadrature.
#
#  Discussion:
#
#    The integral:
#
#      Integral ( -1 <= X <= 1 ) F(X) dX
#
#    The quadrature rule:
#
#      Sum ( 1 <= I <= N ) W(I) * F ( X(I) )
#
#    The quadrature rule will integrate exactly all polynomials up to
#    X^(2*N-3).
#
#    The Lobatto rule is distinguished by the fact that both endpoints
#    (-1 and 1) are always abscissas of the rule.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz, Irene Stegun,
#    Handbook of Mathematical Functions,
#    National Bureau of Standards, 1964.
#
#    Arthur Stroud, Don Secrest,
#    Gaussian Quadrature Formulas,
#    Prentice Hall, 1966.
#
#    Daniel Zwillinger, editor,
#    Standard Mathematical Tables and Formulae,
#    30th Edition,
#    CRC Press, 1996.
#
#  Parameters:
#
#    Input, integer N, the order.
#    N must be between 1 and 20.
#
#    Output, real X(N), the abscissas.
#
#    Output, real W(N), the weights.
#
  import numpy as np
  from sys import exit

  if ( n == 1 ):

    x = np.array ( [ \
           -1.0 ] )

    w = np.array ( [ \
           2.0 ] )

  elif ( n == 2 ):

    x = np.array ( [ \
            - 1.0, \
              1.0 ] )

    w = np.array ( [ \
            1.0, \
            1.0 ] )

  elif ( n == 3 ):

    x = np.array ( [ \
            - 1.0, \
              0.0, \
              1.0 ] )

    w = np.array ( [ \
            1.0 / 3.0, \
            4.0 / 3.0, \
            1.0 / 3.0 ] )

  elif ( n == 4 ):

    x = np.array ( [ \
            - 1.0, \
            - 0.447213595499957939281834733746, \
              0.447213595499957939281834733746, \
              1.0 ] )

    w = np.array ( [ \
            1.0 / 6.0, \
            5.0 / 6.0, \
            5.0 / 6.0, \
            1.0 / 6.0 ] )

  elif ( n == 5 ):

    x = np.array ( [ \
            - 1.0, \
            - 0.654653670707977143798292456247, \
              0.0, \
              0.654653670707977143798292456247, \
              1.0 ] )

    w = np.array ( [ \
            9.0 / 90.0, \
           49.0 / 90.0, \
           64.0 / 90.0, \
           49.0 / 90.0, \
            9.0 / 90.0 ] )

  elif ( n == 6 ):

    x = np.array ( [ \
            - 1.0, \
            - 0.765055323929464692851002973959, \
            - 0.285231516480645096314150994041, \
              0.285231516480645096314150994041, \
              0.765055323929464692851002973959, \
              1.0 ] )

    w = np.array ( [ \
            0.066666666666666666666666666667, \
            0.378474956297846980316612808212, \
            0.554858377035486353016720525121, \
            0.554858377035486353016720525121, \
            0.378474956297846980316612808212, \
            0.066666666666666666666666666667 ] )

  elif ( n == 7 ):

    x = np.array ( [ \
            - 1.0, \
            - 0.830223896278566929872032213967, \
            - 0.468848793470714213803771881909, \
              0.0, \
              0.468848793470714213803771881909, \
              0.830223896278566929872032213967, \
              1.0 ] )

    w = np.array ( [ \
            0.476190476190476190476190476190E-01, \
            0.276826047361565948010700406290, \
            0.431745381209862623417871022281, \
            0.487619047619047619047619047619, \
            0.431745381209862623417871022281, \
            0.276826047361565948010700406290, \
            0.476190476190476190476190476190E-01 ] )

  elif ( n == 8 ):

    x = np.array ( [ \
            - 1.0, \
            - 0.871740148509606615337445761221, \
            - 0.591700181433142302144510731398, \
            - 0.209299217902478868768657260345, \
              0.209299217902478868768657260345, \
              0.591700181433142302144510731398, \
              0.871740148509606615337445761221, \
              1.0 ] )

    w = np.array ( [ \
            0.357142857142857142857142857143E-01, \
            0.210704227143506039382991065776, \
            0.341122692483504364764240677108, \
            0.412458794658703881567052971402, \
            0.412458794658703881567052971402, \
            0.341122692483504364764240677108, \
            0.210704227143506039382991065776, \
            0.357142857142857142857142857143E-01 ] )

  elif ( n == 9 ):

    x = np.array ( [ \
            - 1.0, \
            - 0.899757995411460157312345244418, \
            - 0.677186279510737753445885427091, \
            - 0.363117463826178158710752068709, \
              0.0, \
              0.363117463826178158710752068709, \
              0.677186279510737753445885427091, \
              0.899757995411460157312345244418, \
              1.0 ] )

    w = np.array ( [ \
            0.277777777777777777777777777778E-01, \
            0.165495361560805525046339720029, \
            0.274538712500161735280705618579, \
            0.346428510973046345115131532140, \
            0.371519274376417233560090702948, \
            0.346428510973046345115131532140, \
            0.274538712500161735280705618579, \
            0.165495361560805525046339720029, \
            0.277777777777777777777777777778E-01 ] )

  elif ( n == 10 ):

    x = np.array ( [ \
            - 1.0, \
            - 0.919533908166458813828932660822, \
            - 0.738773865105505075003106174860, \
            - 0.477924949810444495661175092731, \
            - 0.165278957666387024626219765958, \
              0.165278957666387024626219765958, \
              0.477924949810444495661175092731, \
              0.738773865105505075003106174860, \
              0.919533908166458813828932660822, \
              1.0 ] )

    w = np.array ( [ \
            0.222222222222222222222222222222E-01, \
            0.133305990851070111126227170755, \
            0.224889342063126452119457821731, \
            0.292042683679683757875582257374, \
            0.327539761183897456656510527917, \
            0.327539761183897456656510527917, \
            0.292042683679683757875582257374, \
            0.224889342063126452119457821731, \
            0.133305990851070111126227170755, \
            0.222222222222222222222222222222E-01 ] )

  elif ( n == 11 ):

    x = np.array ( [ \
            - 1.0, \
            - 0.934001430408059134332274136099, \
            - 0.784483473663144418622417816108, \
            - 0.565235326996205006470963969478, \
            - 0.295758135586939391431911515559, \
              0.0, \
              0.295758135586939391431911515559, \
              0.565235326996205006470963969478, \
              0.784483473663144418622417816108, \
              0.934001430408059134332274136099, \
              1.0 ] )

    w = np.array ( [ \
            0.181818181818181818181818181818E-01, \
            0.109612273266994864461403449580, \
            0.187169881780305204108141521899, \
            0.248048104264028314040084866422, \
            0.286879124779008088679222403332, \
            0.300217595455690693785931881170, \
            0.286879124779008088679222403332, \
            0.248048104264028314040084866422, \
            0.187169881780305204108141521899, \
            0.109612273266994864461403449580, \
            0.181818181818181818181818181818E-01 ] )

  elif ( n == 12 ):

    x = np.array ( [ \
            - 1.0, \
            - 0.944899272222882223407580138303, \
            - 0.819279321644006678348641581717, \
            - 0.632876153031869677662404854444, \
            - 0.399530940965348932264349791567, \
            - 0.136552932854927554864061855740, \
              0.136552932854927554864061855740, \
              0.399530940965348932264349791567, \
              0.632876153031869677662404854444, \
              0.819279321644006678348641581717, \
              0.944899272222882223407580138303, \
              1.0 ] )

    w = np.array ( [ \
            0.151515151515151515151515151515E-01, \
            0.916845174131961306683425941341E-01, \
            0.157974705564370115164671062700, \
            0.212508417761021145358302077367, \
            0.251275603199201280293244412148, \
            0.271405240910696177000288338500, \
            0.271405240910696177000288338500, \
            0.251275603199201280293244412148, \
            0.212508417761021145358302077367, \
            0.157974705564370115164671062700, \
            0.916845174131961306683425941341E-01, \
            0.151515151515151515151515151515E-01 ] )

  elif ( n == 13 ):

    x = np.array ( [ \
            - 1.0, \
            - 0.953309846642163911896905464755, \
            - 0.846347564651872316865925607099, \
            - 0.686188469081757426072759039566, \
            - 0.482909821091336201746937233637, \
            - 0.249286930106239992568673700374, \
              0.0, \
              0.249286930106239992568673700374, \
              0.482909821091336201746937233637, \
              0.686188469081757426072759039566, \
              0.846347564651872316865925607099, \
              0.953309846642163911896905464755, \
              1.0 ] )

    w = np.array ( [ \
            0.128205128205128205128205128205E-01, \
            0.778016867468189277935889883331E-01, \
            0.134981926689608349119914762589, \
            0.183646865203550092007494258747, \
            0.220767793566110086085534008379, \
            0.244015790306676356458578148360, \
            0.251930849333446736044138641541, \
            0.244015790306676356458578148360, \
            0.220767793566110086085534008379, \
            0.183646865203550092007494258747, \
            0.134981926689608349119914762589, \
            0.778016867468189277935889883331E-01, \
            0.128205128205128205128205128205E-01 ] )

  elif ( n == 14 ):

    x = np.array ( [ \
            - 1.0, \
            - 0.959935045267260901355100162015, \
            - 0.867801053830347251000220202908, \
            - 0.728868599091326140584672400521, \
            - 0.550639402928647055316622705859, \
            - 0.342724013342712845043903403642, \
            - 0.116331868883703867658776709736, \
              0.116331868883703867658776709736, \
              0.342724013342712845043903403642, \
              0.550639402928647055316622705859, \
              0.728868599091326140584672400521, \
              0.867801053830347251000220202908, \
              0.959935045267260901355100162015, \
              1.0 ] )

    w = np.array ( [ \
            0.109890109890109890109890109890E-01, \
            0.668372844976812846340706607461E-01, \
            0.116586655898711651540996670655, \
            0.160021851762952142412820997988, \
            0.194826149373416118640331778376, \
            0.219126253009770754871162523954, \
            0.231612794468457058889628357293, \
            0.231612794468457058889628357293, \
            0.219126253009770754871162523954, \
            0.194826149373416118640331778376, \
            0.160021851762952142412820997988, \
            0.116586655898711651540996670655, \
            0.668372844976812846340706607461E-01, \
            0.109890109890109890109890109890E-01 ] )

  elif ( n == 15 ):

    x = np.array ( [ \
            - 1.0, \
            - 0.965245926503838572795851392070, \
            - 0.885082044222976298825401631482, \
            - 0.763519689951815200704118475976, \
            - 0.606253205469845711123529938637, \
            - 0.420638054713672480921896938739, \
            - 0.215353955363794238225679446273, \
              0.0, \
              0.215353955363794238225679446273, \
              0.420638054713672480921896938739, \
              0.606253205469845711123529938637, \
              0.763519689951815200704118475976, \
              0.885082044222976298825401631482, \
              0.965245926503838572795851392070, \
              1.0 ] )

    w = np.array ( [ \
            0.952380952380952380952380952381E-02, \
            0.580298930286012490968805840253E-01, \
            0.101660070325718067603666170789, \
            0.140511699802428109460446805644, \
            0.172789647253600949052077099408, \
            0.196987235964613356092500346507, \
            0.211973585926820920127430076977, \
            0.217048116348815649514950214251, \
            0.211973585926820920127430076977, \
            0.196987235964613356092500346507, \
            0.172789647253600949052077099408, \
            0.140511699802428109460446805644, \
            0.101660070325718067603666170789, \
            0.580298930286012490968805840253E-01, \
            0.952380952380952380952380952381E-02 ] )

  elif ( n == 16 ):

    x = np.array ( [ \
            - 1.0, \
            - 0.969568046270217932952242738367, \
            - 0.899200533093472092994628261520, \
            - 0.792008291861815063931088270963, \
            - 0.652388702882493089467883219641, \
            - 0.486059421887137611781890785847, \
            - 0.299830468900763208098353454722, \
            - 0.101326273521949447843033005046, \
              0.101326273521949447843033005046, \
              0.299830468900763208098353454722, \
              0.486059421887137611781890785847, \
              0.652388702882493089467883219641, \
              0.792008291861815063931088270963, \
              0.899200533093472092994628261520, \
              0.969568046270217932952242738367, \
              1.0 ] )

    w = np.array ( [ \
            0.833333333333333333333333333333E-02, \
            0.508503610059199054032449195655E-01, \
            0.893936973259308009910520801661E-01, \
            0.124255382132514098349536332657, \
            0.154026980807164280815644940485, \
            0.177491913391704125301075669528, \
            0.193690023825203584316913598854, \
            0.201958308178229871489199125411, \
            0.201958308178229871489199125411, \
            0.193690023825203584316913598854, \
            0.177491913391704125301075669528, \
            0.154026980807164280815644940485, \
            0.124255382132514098349536332657, \
            0.893936973259308009910520801661E-01, \
            0.508503610059199054032449195655E-01, \
            0.833333333333333333333333333333E-02 ] )

  elif ( n == 17 ):

    x = np.array ( [ \
            - 1.0, \
            - 0.973132176631418314156979501874, \
            - 0.910879995915573595623802506398, \
            - 0.815696251221770307106750553238, \
            - 0.691028980627684705394919357372, \
            - 0.541385399330101539123733407504, \
            - 0.372174433565477041907234680735, \
            - 0.189511973518317388304263014753, \
              0.0, \
              0.189511973518317388304263014753, \
              0.372174433565477041907234680735, \
              0.541385399330101539123733407504, \
              0.691028980627684705394919357372, \
              0.815696251221770307106750553238, \
              0.910879995915573595623802506398, \
              0.973132176631418314156979501874, \
              1.0 ] )

    w = np.array ( [ \
            0.735294117647058823529411764706E-02, \
            0.449219405432542096474009546232E-01, \
            0.791982705036871191902644299528E-01, \
            0.110592909007028161375772705220, \
            0.137987746201926559056201574954, \
            0.160394661997621539516328365865, \
            0.177004253515657870436945745363, \
            0.187216339677619235892088482861, \
            0.190661874753469433299407247028, \
            0.187216339677619235892088482861, \
            0.177004253515657870436945745363, \
            0.160394661997621539516328365865, \
            0.137987746201926559056201574954, \
            0.110592909007028161375772705220, \
            0.791982705036871191902644299528E-01, \
            0.449219405432542096474009546232E-01, \
            0.735294117647058823529411764706E-02 ] )

  elif ( n == 18 ):

    x = np.array ( [ \
            - 1.0, \
            - 0.976105557412198542864518924342, \
            - 0.920649185347533873837854625431, \
            - 0.835593535218090213713646362328, \
            - 0.723679329283242681306210365302, \
            - 0.588504834318661761173535893194, \
            - 0.434415036912123975342287136741, \
            - 0.266362652878280984167665332026, \
            - 0.897490934846521110226450100886E-01, \
              0.897490934846521110226450100886E-01, \
              0.266362652878280984167665332026, \
              0.434415036912123975342287136741, \
              0.588504834318661761173535893194, \
              0.723679329283242681306210365302, \
              0.835593535218090213713646362328, \
              0.920649185347533873837854625431, \
              0.976105557412198542864518924342, \
              1.0 ] )

    w = np.array ( [ \
            0.653594771241830065359477124183E-02, \
            0.399706288109140661375991764101E-01, \
            0.706371668856336649992229601678E-01, \
            0.990162717175028023944236053187E-01, \
            0.124210533132967100263396358897, \
            0.145411961573802267983003210494, \
            0.161939517237602489264326706700, \
            0.173262109489456226010614403827, \
            0.179015863439703082293818806944, \
            0.179015863439703082293818806944, \
            0.173262109489456226010614403827, \
            0.161939517237602489264326706700, \
            0.145411961573802267983003210494, \
            0.124210533132967100263396358897, \
            0.990162717175028023944236053187E-01, \
            0.706371668856336649992229601678E-01, \
            0.399706288109140661375991764101E-01, \
            0.653594771241830065359477124183E-02 ] )

  elif ( n == 19 ):

    x = np.array ( [ \
            - 1.0, \
            - 0.978611766222080095152634063110, \
            - 0.928901528152586243717940258797, \
            - 0.852460577796646093085955970041, \
            - 0.751494202552613014163637489634, \
            - 0.628908137265220497766832306229, \
            - 0.488229285680713502777909637625, \
            - 0.333504847824498610298500103845, \
            - 0.169186023409281571375154153445, \
              0.0, \
              0.169186023409281571375154153445, \
              0.333504847824498610298500103845, \
              0.488229285680713502777909637625, \
              0.628908137265220497766832306229, \
              0.751494202552613014163637489634, \
              0.852460577796646093085955970041, \
              0.928901528152586243717940258797, \
              0.978611766222080095152634063110, \
              1.0 ] )

    w = np.array ( [ \
            0.584795321637426900584795321637E-02, \
            0.357933651861764771154255690351E-01, \
            0.633818917626297368516956904183E-01, \
            0.891317570992070844480087905562E-01, \
            0.112315341477305044070910015464, \
            0.132267280448750776926046733910, \
            0.148413942595938885009680643668, \
            0.160290924044061241979910968184, \
            0.167556584527142867270137277740, \
            0.170001919284827234644672715617, \
            0.167556584527142867270137277740, \
            0.160290924044061241979910968184, \
            0.148413942595938885009680643668, \
            0.132267280448750776926046733910, \
            0.112315341477305044070910015464, \
            0.891317570992070844480087905562E-01, \
            0.633818917626297368516956904183E-01, \
            0.357933651861764771154255690351E-01, \
            0.584795321637426900584795321637E-02 ] )

  elif ( n == 20 ):

    x = np.array ( [ \
            - 1.0, \
            - 0.980743704893914171925446438584, \
            - 0.935934498812665435716181584931, \
            - 0.866877978089950141309847214616, \
            - 0.775368260952055870414317527595, \
            - 0.663776402290311289846403322971, \
            - 0.534992864031886261648135961829, \
            - 0.392353183713909299386474703816, \
            - 0.239551705922986495182401356927, \
            - 0.805459372388218379759445181596E-01, \
              0.805459372388218379759445181596E-01, \
              0.239551705922986495182401356927, \
              0.392353183713909299386474703816, \
              0.534992864031886261648135961829, \
              0.663776402290311289846403322971, \
              0.775368260952055870414317527595, \
              0.866877978089950141309847214616, \
              0.935934498812665435716181584931, \
              0.980743704893914171925446438584, \
              1.0 ] )

    w = np.array ( [ \
            0.526315789473684210526315789474E-02, \
            0.322371231884889414916050281173E-01, \
            0.571818021275668260047536271732E-01, \
            0.806317639961196031447768461137E-01, \
            0.101991499699450815683781205733, \
            0.120709227628674725099429705002, \
            0.136300482358724184489780792989, \
            0.148361554070916825814713013734, \
            0.156580102647475487158169896794, \
            0.160743286387845749007726726449, \
            0.160743286387845749007726726449, \
            0.156580102647475487158169896794, \
            0.148361554070916825814713013734, \
            0.136300482358724184489780792989, \
            0.120709227628674725099429705002, \
            0.101991499699450815683781205733, \
            0.806317639961196031447768461137E-01, \
            0.571818021275668260047536271732E-01, \
            0.322371231884889414916050281173E-01, \
            0.526315789473684210526315789474E-02 ] )

  else:

    print ( '' )
    print ( 'LOBATTO_SET - Fatal error!' )
    print ( '  Illegal value of N = %d' % ( n ) )
    print ( '  Legal values are between 1 and 20.' )
    exit ( 'LOBATTO_SET - Fatal error!' )

  return x, w

def lobatto_set_test ( ):

#*****************************************************************************80
#
## LOBATTO_SET_TEST tests LOBATTO_SET.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    09 June 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'LOBATTO_SET_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  LOBATTO_SET sets a Lobatto rule' )
  print ( '' )
  print ( '         I      X             W' )

  for n in range ( 4, 11, 3 ):

    x, w = lobatto_set ( n )

    print ( '' )
    for i in range ( 0, n ):
      print ( '  %8d  %12g  %12g' % ( i, x[i], w[i] ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'LOBATTO_SET_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  lobatto_set_test ( )
  timestamp ( )

#! /usr/bin/env python3
#


def a_log(rule):

    # *****************************************************************************80
    #
    # A_LOG returns the value of A for an Alpert rule for log singular functions.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer RULE, the index of the rule, between 1 and 10.
    #
    #    Output, integer A, the value of A.
    #
    import numpy as np
    from sys import exit

    a_vec = np.array([
        1, 2, 2, 3, 3,
        5, 6, 7, 9, 10])

    if (rule < 1 or 10 < rule):
        print('')
        print('A_LOG - Fatal error!')
        print('  Input value of RULE is not between 1 and 10.')
        exit('A_LOG - Fatal error!')
    a = a_vec[rule - 1]

    return a


def j_log(rule):

    # *****************************************************************************80
    #
    # J_LOG returns the value of J for an Alpert rule for log singular functions.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer RULE, the index of the rule, between 1 and 10.
    #
    #    Output, integer J, the value of J.
    #
    import numpy as np
    from sys import exit

    j_vec = np.array([
        1, 2, 3, 4, 5,
        7, 10, 11, 14, 15])

    if (rule < 1 or 10 < rule):
        print('')
        print('J_LOG - Fatal error!')
        print('  Input value of RULE is not between 1 and 10.')
        exit('J_LOG - Fatal error!')

    j = j_vec[rule - 1]

    return j


def num_log():

    # *****************************************************************************80
    #
    # NUM_LOG returns the number of Alpert rules for log singular functions.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Output, integer NUM, the number of rules.
    #
    num = 10

    return num


def order_log(rule):

    # *****************************************************************************80
    #
    # ORDER_LOG returns the order of an Alpert rule for log singular functions.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer RULE, the index of the rule, between 1 and 10.
    #
    #    Output, integer ORDER, the order of the rule.
    #
    import numpy as np
    from sys import exit

    order_vec = np.array([
        2, 3, 4, 5, 6,
        8, 10, 12, 14, 16])

    if (rule < 1 or 10 < rule):
        print('')
        print('ORDER_LOG - Fatal error!')
        print('  Input value of RULE is not between 1 and 10.')
        exit('ORDER_LOG - Fatal error!')

    order = order_vec[rule - 1]

    return order


def rule_log(rule, j):

    # *****************************************************************************80
    #
    # RULE_LOG returns an Alpert rule for log singular functions.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    Bradley Alpert,
    #    Hybrid Gauss-Trapezoidal Quadrature Rules,
    #    SIAM Journal on Scientific Computing,
    #    Volume 20, Number 5, pages 1551-1584, 1999.
    #
    #  Parameters:
    #
    #    Input, integer RULE, the index of the rule, between 1 and 10.
    #
    #    Input, integer J, the number of points in the rule.
    #
    #    Output, real X[J], W[J], the points and weights needed for the rule.
    #
    import numpy as np
    from sys import exit

    if (rule < 1 or 10 < rule):
        print('')
        print('RULE_LOG - Fatal error!')
        print('  Input value of RULE is not between 1 and 10.')
        exit('RULE_LOG - Fatal error!')

    if (rule == 1):

        x = np.array([
            1.591549430918953E-01])

        w = np.array([
            5.0E-01])

    elif (rule == 2):

        x = np.array([
            1.150395811972836E-01,
            9.365464527949632E-01])

        w = np.array([
            3.913373788753340E-01,
            1.108662621124666E+00])

    elif (rule == 3):

        x = np.array([
            2.379647284118974E-02,
            2.935370741501914E-01,
            1.023715124251890E+00])

        w = np.array([
            8.795942675593887E-02,
            4.989017152913699E-01,
            9.131388579526912E-01])

    elif (rule == 4):

        x = np.array([
            2.339013027203800E-02,
            2.854764931311984E-01,
            1.005403327220700E+00,
            1.994970303994294E+00])

        w = np.array([
            8.609736556158105E-02,
            4.847019685417959E-01,
            9.152988869123725E-01,
            1.013901778984250E+00])

    elif (rule == 5):

        x = np.array([
            4.004884194926570E-03,
            7.745655373336686E-02,
            3.972849993523248E-01,
            1.075673352915104E+00,
            2.003796927111872E+00])

        w = np.array([
            1.671879691147102E-02,
            1.636958371447360E-01,
            4.981856569770637E-01,
            8.372266245578912E-01,
            9.841730844088381E-01])

    elif (rule == 6):

        x = np.array([
            6.531815708567918E-03,
            9.086744584657729E-02,
            3.967966533375878E-01,
            1.027856640525646E+00,
            1.945288592909266E+00,
            2.980147933889640E+00,
            3.998861349951123E+00])

        w = np.array([
            2.462194198995203E-02,
            1.701315866854178E-01,
            4.609256358650077E-01,
            7.947291148621894E-01,
            1.008710414337933E+00,
            1.036093649726216E+00,
            1.004787656533285E+00])

    elif (rule == 7):

        x = np.array([
            1.175089381227308E-03,
            1.877034129831289E-02,
            9.686468391426860E-02,
            3.004818668002884E-01,
            6.901331557173356E-01,
            1.293695738083659E+00,
            2.090187729798780E+00,
            3.016719313149212E+00,
            4.001369747872486E+00,
            5.000025661793423E+00])

        w = np.array([
            4.560746882084207E-03,
            3.810606322384757E-02,
            1.293864997289512E-01,
            2.884360381408835E-01,
            4.958111914344961E-01,
            7.077154600594529E-01,
            8.741924365285083E-01,
            9.661361986515218E-01,
            9.957887866078700E-01,
            9.998665787423845E-01])

    elif (rule == 8):

        x = np.array([
            1.674223682668368E-03,
            2.441110095009738E-02,
            1.153851297429517E-01,
            3.345898490480388E-01,
            7.329740531807683E-01,
            1.332305048525433E+00,
            2.114358752325948E+00,
            3.026084549655318E+00,
            4.003166301292590E+00,
            5.000141170055870E+00,
            6.000001002441859E+00])

        w = np.array([
            6.364190780720557E-03,
            4.723964143287529E-02,
            1.450891158385963E-01,
            3.021659470785897E-01,
            4.984270739715340E-01,
            6.971213795176096E-01,
            8.577295622757315E-01,
            9.544136554351155E-01,
            9.919938052776484E-01,
            9.994621875822987E-01,
            9.999934408092805E-01])

    elif (rule == 9):

        x = np.array([
            9.305182368545380E-04,
            1.373832458434617E-02,
            6.630752760779359E-02,
            1.979971397622003E-01,
            4.504313503816532E-01,
            8.571888631101634E-01,
            1.434505229617112E+00,
            2.175177834137754E+00,
            3.047955068386372E+00,
            4.004974906813428E+00,
            4.998525901820967E+00,
            5.999523015116678E+00,
            6.999963617883990E+00,
            7.999999488130134E+00])

        w = np.array([
            3.545060644780164E-03,
            2.681514031576498E-02,
            8.504092035093420E-02,
            1.854526216643691E-01,
            3.251724374883192E-01,
            4.911553747260108E-01,
            6.622933417369036E-01,
            8.137254578840510E-01,
            9.235595514944174E-01,
            9.821609923744658E-01,
            1.000047394596121E+00,
            1.000909336693954E+00,
            1.000119534283784E+00,
            1.000002835746089E+00])

    elif (rule == 10):

        x = np.array([
            8.371529832014113E-04,
            1.239382725542637E-02,
            6.009290785739468E-02,
            1.805991249601928E-01,
            4.142832599028031E-01,
            7.964747731112430E-01,
            1.348993882467059E+00,
            2.073471660264395E+00,
            2.947904939031494E+00,
            3.928129252248612E+00,
            4.957203086563112E+00,
            5.986360113977494E+00,
            6.997957704791519E+00,
            7.999888757524622E+00,
            8.999998754306120E+00])

        w = np.array([
            3.190919086626234E-03,
            2.423621380426338E-02,
            7.740135521653088E-02,
            1.704889420286369E-01,
            3.029123478511309E-01,
            4.652220834914617E-01,
            6.401489637096768E-01,
            8.051212946181061E-01,
            9.362411945698647E-01,
            1.014359775369075E+00,
            1.035167721053657E+00,
            1.020308624984610E+00,
            1.004798397441514E+00,
            1.000395017352309E+00,
            1.000007149422537E+00])

    return x, w


def alpert_log_test():

    # *****************************************************************************80
    #
    # ALPERT_LOG_TEST tests the Alpert rule on the log integrand.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np

    print('')
    print('ALPERT_LOG_TEST')
    print('  Test the Alpert rule on the log integrand.')
    print('')
    print('  Rule    Order   J   A        N     N+2J               H        Estimate           Error')
    print('')

    v2 = integral_log()

    num_l = num_log()
#
#  For the righthand interval, use the regular rule of the same index.
#
    for rule in range(1, num_l + 1):

        a_l = a_log(rule)
        j_l = j_log(rule)
        order_l = order_log(rule)
        x_l, w_l = rule_log(rule, j_l)

        a_r = a_regular(rule)
        j_r = j_regular(rule)
        order_r = order_regular(rule)
        x_r, w_r = rule_regular(rule, j_r)

        n = 8

        for nlog in range(4, 8):

            n = n * 2
            h = 1.0 / float(n + a_l + a_r - 1)

            x1 = h * x_l
            f1 = integrand_log(j_l, x1)
            s1 = np.dot(w_l, f1)

            x2 = np.linspace(a_l * h, (a_l + n - 1) * h, n)
            f2 = integrand_log(n, x2)
            s2 = np.sum(f2)

            x3 = 1.0 - h * x_r
            f3 = integrand_log(j_r, x3)
            s3 = np.dot(w_r, f3)

            v1 = h * (s1 + s2 + s3)

            print('    %2d     %4.1f  %2d  %2d  %7d  %7d  %14.6g  %14.6g  %14.6g'
                  % (rule, order_l, j_l, a_l, n, n + j_l + j_r, h, v1, abs(v1 - v2)))

        print('')

    print('')
    print('                                                    Exact: %14.6g' % (v2))
#
#  Terminate.
#
    print('')
    print('ALPERT_LOG_TEST')
    print('  Normal end of execution.')
    return


def a_power(rule):

    # *****************************************************************************80
    #
    # A_POWER returns the value of A for an Alpert rule for power singular functions.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer RULE, the index of the rule, between 1 and 12.
    #
    #    Output, integer A, the value of A.
    #
    import numpy as np
    from sys import exit

    a_vec = np.array([
        1, 2, 2, 2, 2,
        3, 4, 5, 6, 8,
        9, 10])

    if (rule < 1 or 12 < rule):
        print('')
        print('A_POWER - Fatal error!')
        print('  Input value of RULE is not between 1 and 12.')
        exit('A_POWER - Fatal error!')

    a = a_vec[rule - 1]

    return a


def j_power(rule):

    # *****************************************************************************80
    #
    # J_POWER returns the value of J for an Alpert rule for power singular functions.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer RULE, the index of the rule, between 1 and 12.
    #
    #    Output, integer J, the value of J.
    #
    import numpy as np
    from sys import exit

    j_vec = np.array([
        1, 2, 2, 3, 3,
        4, 6, 8, 10, 12,
        14, 16])

    if (rule < 1 or 12 < rule):
        print('')
        print('J_POWER - Fatal error!')
        print('  Input value of RULE is not between 1 and 12.')
        exit('J_POWER - Fatal error!')

    j = j_vec[rule - 1]

    return j


def num_power():

    # *****************************************************************************80
    #
    # NUM_POWER returns the number of Alpert rules for power singular functions.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Output, integer NUM, the number of rules.
    #
    num = 12

    return num


def order_power(rule):

    # *****************************************************************************80
    #
    # ORDER_POWER returns the order of an Alpert rule for power singular functions.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer RULE, the index of the rule, between 1 and 10.
    #
    #    Output, real ORDER, the order of the rule.
    #
    import numpy as np
    from sys import exit

    order_vec = np.array([
        1.5, 2.0, 2.5, 3.0, 3.5,
        4.0, 6.0, 8.0, 10.0, 12.0,
        14.0, 16.0])

    if (rule < 1 or 12 < rule):
        print('')
        print('ORDER_POWER - Fatal error!')
        print('  Input value of RULE is not between 1 and 12.')
        exit('ORDER_POWER - Fatal error!')

    order = order_vec[rule - 1]

    return order


def rule_power(rule, j):

    # *****************************************************************************80
    #
    # RULE_POWER returns an Alpert rule for power singular functions.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    Bradley Alpert,
    #    Hybrid Gauss-Trapezoidal Quadrature Rules,
    #    SIAM Journal on Scientific Computing,
    #    Volume 20, Number 5, pages 1551-1584, 1999.
    #
    #  Parameters:
    #
    #    Input, integer RULE, the index of the rule, between 1 and 12.
    #
    #    Input, integer J, the number of points in the rule.
    #
    #    Output, real X[J], W[J], the points and weights needed for the rule.
    #
    import numpy as np
    from sys import exit

    if (rule < 1 or 12 < rule):
        print('')
        print('RULE_POWER - Fatal error!')
        print('  Input value of RULE is not between 1 and 12.')
        exit('RULE_POWER - Fatal error!')

    if (rule == 1):

        x = np.array([
            1.172258571393266E-01])

        w = np.array([
            5.000000000000000E-01])

    elif (rule == 2):

        x = np.array([
            9.252112715421378E-02,
            1.000000000000000E-00])

        w = np.array([
            4.198079625266162E-01,
            1.080192037473384E+00])

    elif (rule == 3):

        x = np.array([
            6.023873796408450E-02,
            8.780704050676215E-01])

        w = np.array([
            2.858439990420468E-01,
            1.214156000957953E+00])

    elif (rule == 4):

        x = np.array([
            7.262978413470474E-03,
            2.246325512521893E-01,
            1.000000000000000E+00])

        w = np.array([
            3.907638767531813E-02,
            4.873484056646474E-01,
            9.735752066600344E-01])

    elif (rule == 5):

        x = np.array([
            1.282368909458828E-02,
            2.694286346792474E-01,
            1.018414523786358E+00])

        w = np.array([
            6.363996663105925E-02,
            5.077434578043636E-01,
            9.286165755645772E-01])

    elif (rule == 6):

        x = np.array([
            1.189242434021285E-02,
            2.578220434738662E-01,
            1.007750064585281E+00,
            2.000000000000000E+00])

        w = np.array([
            5.927215035616424E-02,
            4.955981740306228E-01,
            9.427131290628058E-01,
            1.002416546550407E+00])

    elif (rule == 7):

        x = np.array([
            3.317925942699451E-03,
            8.283019705296352E-02,
            4.136094925726231E-01,
            1.088744373688402E+00,
            2.006482101852379E+00,
            3.000000000000000E+00])

        w = np.array([
            1.681780929883469E-02,
            1.755244404544475E-01,
            5.039350503858001E-01,
            8.266241339680867E-01,
            9.773065848981277E-01,
            9.997919809947032E-01])

    elif (rule == 8):

        x = np.array([
            1.214130606523435E-03,
            3.223952700027058E-02,
            1.790935383649920E-01,
            5.437663805244631E-01,
            1.176116628396759E+00,
            2.031848210716014E+00,
            3.001961225690812E+00,
            4.000000000000000E+00])

        w = np.array([
            6.199844884297793E-03,
            7.106286791720044E-02,
            2.408930104410471E-01,
            4.975929263668960E-01,
            7.592446540441226E-01,
            9.322446399614420E-01,
            9.928171438160095E-01,
            9.999449125689846E-01])

    elif (rule == 9):

        x = np.array([
            1.745862989163252E-04,
            8.613670540457314E-03,
            6.733385088703690E-02,
            2.514488774733840E-01,
            6.341845573737690E-01,
            1.248404055083152E+00,
            2.065688031953401E+00,
            3.009199358662542E+00,
            4.000416269690208E+00,
            5.000000000000000E+00])

        w = np.array([
            1.016950985948944E-03,
            2.294670686517670E-02,
            1.076657968022888E-01,
            2.734577662465576E-01,
            4.978815591924992E-01,
            7.256208919565360E-01,
            8.952638690320078E-01,
            9.778157465381624E-01,
            9.983390781399277E-01,
            9.999916342408948E-01])

    elif (rule == 10):

        x = np.array([
            5.710218427206990E-04,
            1.540424351115548E-02,
            8.834248407196555E-02,
            2.824462054509770E-01,
            6.574869892305580E-01,
            1.246541060977993E+00,
            2.039218495130811E+00,
            2.979333487049800E+00,
            3.985772595393049E+00,
            4.997240804311428E+00,
            5.999868793951190E+00,
            7.000000000000000E+00])

        w = np.array([
            2.921018926912141E-03,
            3.431130611256885E-02,
            1.224669495638615E-01,
            2.761108242022520E-01,
            4.797809643010337E-01,
            6.966555677271379E-01,
            8.790077941972658E-01,
            9.868622449294327E-01,
            1.015142389688201E+00,
            1.006209712632210E+00,
            1.000528829922287E+00,
            1.000002397796838E+00])

    elif (rule == 11):

        x = np.array([
            3.419821460249725E-04,
            9.296593430187960E-03,
            5.406214771755252E-02,
            1.763945096508648E-01,
            4.218486605653738E-01,
            8.274022895884040E-01,
            1.410287585637014E+00,
            2.160997505238153E+00,
            3.043504749358223E+00,
            4.005692579069439E+00,
            4.999732707905968E+00,
            5.999875191971098E+00,
            6.999994560568667E+00,
            8.000000000000000E+00])

        w = np.array([
            1.750957243202047E-03,
            2.080726584287380E-02,
            7.586830616433430E-02,
            1.766020526671851E-01,
            3.206624362072232E-01,
            4.934405290553812E-01,
            6.707497030698472E-01,
            8.244959025366557E-01,
            9.314646742162802E-01,
            9.845768443163154E-01,
            9.992852769154770E-01,
            1.000273112957723E+00,
            1.000022857402321E+00,
            1.000000081405180E+00])

    elif (rule == 12):

        x = np.array([
            2.158438988280793E-04,
            5.898432743709196E-03,
            3.462795956896131E-02,
            1.145586495070213E-01,
            2.790344218856415E-01,
            5.600113798653321E-01,
            9.814091242883119E-01,
            1.553594853974655E+00,
            2.270179114036658E+00,
            3.108234601715371E+00,
            4.032930893996553E+00,
            5.006803270228157E+00,
            6.000815466735179E+00,
            7.000045035079542E+00,
            8.000000738923901E+00,
            9.000000000000000E+00])

        w = np.array([
            1.105804873501181E-03,
            1.324499944707956E-02,
            4.899842307592144E-02,
            1.165326192868815E-01,
            2.178586693194957E-01,
            3.481766016945031E-01,
            4.964027915911545E-01,
            6.469026189623831E-01,
            7.823688971783889E-01,
            8.877772445893361E-01,
            9.551665077035583E-01,
            9.876285579741800E-01,
            9.979929183863017E-01,
            9.998470620634641E-01,
            9.999962891645340E-01,
            9.999999946893169E-01])

    return x, w


def alpert_power_test():

    # *****************************************************************************80
    #
    # ALPERT_POWER_TEST tests the Alpert rule on the power integrand.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np

    print('')
    print('ALPERT_POWER_TEST')
    print('  Test the Alpert rule on the power integrand.')
    print('')
    print('  Rule    Order   J   A        N     N+2J               H        Estimate           Error')
    print('')

    v2 = integral_power()

    num_p = num_power()
#
#  For the righthand interval, use the regular rule of the same index.
#
    for rule in range(1, num_p + 1):

        a_p = a_power(rule)
        j_p = j_power(rule)
        order_p = order_power(rule)
        x_p, w_p = rule_power(rule, j_p)

        a_r = a_regular(rule)
        j_r = j_regular(rule)
        order_r = order_regular(rule)
        x_r, w_r = rule_regular(rule, j_r)

        n = 8

        for nlog in range(4, 7):

            n = n * 2
            h = 1.0 / float(n + a_p + a_r - 1)

            x1 = h * x_p
            f1 = integrand_power(j_p, x1)
            s1 = np.dot(w_p, f1)

            x2 = np.linspace(a_p * h, (a_p + n - 1) * h, n)
            f2 = integrand_power(n, x2)
            s2 = sum(f2)

            x3 = 1.0 - h * x_r
            f3 = integrand_power(j_r, x3)
            s3 = np.dot(w_r, f3)

            v1 = h * (s1 + s2 + s3)

            print('    %2d     %4.1f  %2d  %2d  %7d  %7d  %14.6g  %14.6g  %14.6g'
                  % (rule, order_p, j_p, a_p, n, n + j_p + j_r, h, v1, abs(v1 - v2)))

        print('')

    print('')
    print('                                                    Exact: %14.6g' % (v2))
#
#  Terminate.
#
    print('')
    print('ALPERT_POWER_TEST')
    print('  Normal end of execution.')
    return


def a_regular(rule):

    # *****************************************************************************80
    #
    # A_REGULAR returns the value of A for an Alpert rule for regular functions.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer RULE, the index of the rule, between 1 and 12.
    #
    #    Output, integer A, the value of A.
    #
    import numpy as np
    from sys import exit

    a_vec = np.array([
        1, 2, 2, 3, 3,
        4, 5, 7, 9, 10,
        12, 14])

    if (rule < 1 or 12 < rule):
        print('')
        print('A_REGULAR - Fatal error!')
        print('  Input value of RULE is not between 1 and 12.')
        exit('A_REGULAR - Fatal error!')

    a = a_vec[rule - 1]

    return a


def j_regular(rule):

    # *****************************************************************************80
    #
    # J_REGULAR returns the value of J for an Alpert rule for regular functions.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer RULE, the index of the rule, between 1 and 12.
    #
    #    Output, integer J, the value of J.
    #
    import numpy as np
    from sys import exit

    j_vec = np.array([
        1, 2, 2, 3, 3,
        4, 6, 8, 10, 12,
        14, 16])

    if (rule < 1 or 12 < rule):
        print('')
        print('J_REGULAR - Fatal error!')
        print('  Input value of RULE is not between 1 and 12.')
        exit('J_REGULAR - Fatal error!')

    j = j_vec[rule - 1]

    return j


def num_regular():

    # *****************************************************************************80
    #
    # NUM_REGULAR returns the number of Alpert rules for regular functions.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Output, integer NUM, the number of rules.
    #
    num = 12

    return num


def order_regular(rule):

    # *****************************************************************************80
    #
    # ORDER_REGULAR returns the order of an Alpert rule for regular functions.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer RULE, the index of the rule, between 1 and 12.
    #
    #    Output, integer ORDER, the order of the rule.
    #
    import numpy as np
    from sys import exit

    order_vec = np.array([
        3, 4, 5, 6, 7,
        8, 12, 16, 20, 24,
        28, 32])

    if (rule < 1 or 12 < rule):
        print('')
        print('ORDER_REGULAR - Fatal error!')
        print('  Input value of RULE is not between 1 and 12.')
        exit('ORDER_REGULAR - Fatal error!')

    order = order_vec[rule - 1]

    return order


def rule_regular(rule, j):

    # *****************************************************************************80
    #
    # RULE_REGULAR returns an Alpert rule for regular functions.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    Bradley Alpert,
    #    Hybrid Gauss-Trapezoidal Quadrature Rules,
    #    SIAM Journal on Scientific Computing,
    #    Volume 20, Number 5, pages 1551-1584, 1999.
    #
    #  Parameters:
    #
    #    Input, integer RULE, the index of the rule, between 1 and 12.
    #
    #    Input, integer J, the number of points in the rule.
    #
    #    Output, real X[J], W[J], the points and weights needed for the rule.
    #
    import numpy as np
    from sys import exit

    if (rule < 1 or 12 < rule):
        print('')
        print('RULE_REGULAR - Fatal error!')
        print('  Input value of RULE is not between 1 and 12.')
        exit('RULE_REGULAR - Fatal error!')

    if (rule == 1):

        x = np.array([
            1.666666666666667E-01])

        w = np.array([
            5.000000000000000E-01])

    elif (rule == 2):

        x = np.array([
            2.000000000000000E-01,
            1.000000000000000E+00])

        w = np.array([
            5.208333333333333E-01,
            9.791666666666667E-01])

    elif (rule == 3):

        x = np.array([
            2.245784979812614E-01,
            1.013719374359164E+00])

        w = np.array([
            5.540781643606372E-01,
            9.459218356393628E-01])

    elif (rule == 4):

        x = np.array([
            2.250991042610971E-01,
            1.014269060987992E+00,
            2.000000000000000E+00])

        w = np.array([
            5.549724327164180E-01,
            9.451317411845473E-01,
            9.998958260990347E-01])

    elif (rule == 5):

        x = np.array([
            2.180540672543505E-01,
            1.001181873031216E+00,
            1.997580526418033E+00])

        w = np.array([
            5.408088967208193E-01,
            9.516615045823566E-01,
            1.007529598696824E+00])

    elif (rule == 6):

        x = np.array([
            2.087647422032129E-01,
            9.786087373714483E-01,
            1.989541386579751E+00,
            3.000000000000000E+00])

        w = np.array([
            5.207988277246498E-01,
            9.535038018555888E-01,
            1.024871626402471E+00,
            1.000825744017291E+00])

    elif (rule == 7):

        x = np.array([
            7.023955461621939E-02,
            4.312297857227970E-01,
            1.117752734518115E+00,
            2.017343724572518E+00,
            3.000837842847590E+00,
            4.000000000000000E+00])

        w = np.array([
            1.922315977843698E-01,
            5.348399530514687E-01,
            8.170209442488760E-01,
            9.592111521445966E-01,
            9.967143408044999E-01,
            9.999820119661890E-01])

    elif (rule == 8):

        x = np.array([
            9.919337841451028E-02,
            5.076592669645529E-01,
            1.184972925827278E+00,
            2.047493467134072E+00,
            3.007168911869310E+00,
            4.000474996776184E+00,
            5.000007879022339E+00,
            6.000000000000000E+00])

        w = np.array([
            2.528198928766921E-01,
            5.550158230159486E-01,
            7.852321453615224E-01,
            9.245915673876714E-01,
            9.839350200445296E-01,
            9.984463448413151E-01,
            9.999592378464547E-01,
            9.999999686258662E-01])

    elif (rule == 9):

        x = np.array([
            9.209200446233291E-02,
            4.752021947758861E-01,
            1.124687945844539E+00,
            1.977387385642367E+00,
            2.953848957822108E+00,
            3.976136786048776E+00,
            4.994354281979877E+00,
            5.999469539335291E+00,
            6.999986704874333E+00,
            8.000000000000000E+00])

        w = np.array([
            2.351836144643984E-01,
            5.248820509085946E-01,
            7.634026409869887E-01,
            9.284711336658351E-01,
            1.010969886587741E+00,
            1.024959725311073E+00,
            1.010517534639652E+00,
            1.001551595797932E+00,
            1.000061681794188E+00,
            1.000000135843597E+00])

    elif (rule == 10):

        x = np.array([
            6.001064731474805E-02,
            3.149685016229433E-01,
            7.664508240518316E-01,
            1.396685781342510E+00,
            2.175195903206602E+00,
            3.062320575880355E+00,
            4.016440988792476E+00,
            5.002872064275734E+00,
            6.000285453310164E+00,
            7.000012964962529E+00,
            8.000000175554469E+00,
            9.000000000000000E+00])

        w = np.array([
            1.538932104518340E-01,
            3.551058128559424E-01,
            5.449200036280007E-01,
            7.104078497715549E-01,
            8.398780940253654E-01,
            9.272767950890611E-01,
            9.750605697371132E-01,
            9.942629650823470E-01,
            9.992421778421898E-01,
            9.999534370786161E-01,
            9.999990854912925E-01,
            9.999999989466828E-01])

    elif (rule == 11):

        x = np.array([
            6.234360533194102E-02,
            3.250286721702614E-01,
            7.837350794282182E-01,
            1.415673112616924E+00,
            2.189894250061313E+00,
            3.070053877483040E+00,
            4.018613756218047E+00,
            5.002705902035397E+00,
            5.999929741810400E+00,
            6.999904720846024E+00,
            7.999986894843540E+00,
            8.999999373380393E+00,
            9.999999992002911E+00,
            1.100000000000000E+01])

        w = np.array([
            1.595975279734157E-01,
            3.637046028193864E-01,
            5.498753177297441E-01,
            7.087986792086956E-01,
            8.335172275501195E-01,
            9.204446510608518E-01,
            9.710881776552090E-01,
            9.933296578555239E-01,
            9.994759087910050E-01,
            1.000133030254421E+00,
            1.000032915011460E+00,
            1.000002261653775E+00,
            1.000000042393520E+00,
            1.000000000042872E+00])

    elif (rule == 12):

        x = np.array([
            5.899550614325259E-02,
            3.082757062227814E-01,
            7.463707253079130E-01,
            1.355993726494664E+00,
            2.112943217346336E+00,
            2.987241496545946E+00,
            3.944798920961176E+00,
            4.950269202842798E+00,
            5.972123043117706E+00,
            6.989783558137742E+00,
            7.997673019512965E+00,
            8.999694932747039E+00,
            9.999979225211805E+00,
            1.099999938266130E+01,
            1.199999999462073E+01,
            1.300000000000000E+01])

        w = np.array([
            1.511076023874179E-01,
            3.459395921169090E-01,
            5.273502805146873E-01,
            6.878444094543021E-01,
            8.210319140034114E-01,
            9.218382875515803E-01,
            9.873027487553060E-01,
            1.018251913441155E+00,
            1.021933430349293E+00,
            1.012567983413513E+00,
            1.004052289554521E+00,
            1.000713413344501E+00,
            1.000063618302950E+00,
            1.000002486385216E+00,
            1.000000030404477E+00,
            1.000000000020760E+00])

    return x, w


def alpert_regular_test():

    # *****************************************************************************80
    #
    # ALPERT_REGULAR_TEST tests the Alpert rule on the regular integrand.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np

    print('')
    print('ALPERT_REGULAR_TEST')
    print('  Test the Alpert rule on the regular integrand.')
    print('')
    print('  Rule  Order   J   A        N     N+2J               H        Estimate           Error')
    print('')

    v2 = integral_regular()

    num_r = num_regular()

    for rule in range(1, num_r + 1):

        a = a_regular(rule)
        j = j_regular(rule)
        order = order_regular(rule)
        x, w = rule_regular(rule, j)

        n = 8

        for nlog in range(4, 7):

            n = n * 2
            h = 1.0 / float(n + 2 * a - 1)

            x1 = h * x
            f1 = integrand_regular(j, x1)
            s1 = np.dot(w, f1)

            x2 = np.linspace(a * h, (a + n - 1) * h, n)
            f2 = integrand_regular(n, x2)
            s2 = np.sum(f2)

            x3 = 1.0 - h * x
            f3 = integrand_regular(j, x3)
            s3 = np.dot(w, f3)

            v1 = h * (s1 + s2 + s3)

            print('    %2d     %2d  %2d  %2d  %7d  %7d  %14.6g  %14.6g  %14.6g'
                  % (rule, order, j, a, n, n + 2 * j, h, v1, abs(v1 - v2)))

        print('')

    print('')
    print('                                                  Exact: %14.6g' % (v2))
#
#  Terminate.
#
    print('')
    print('ALPERT_REGULAR_TEST')
    print('  Normal end of execution.')
    return


def alpert_rule_test():

    # *****************************************************************************80
    #
    # ALPERT_RULE_TEST tests the ALPERT_RULE library.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    print('')
    print('ALPERT_RULE_TEST')
    print('  Python version:')
    print('  Test ALPERT_RULE.')
#
#  Utilities.
#
    integral_log_test()
    integral_power_test()
    integral_regular_test()

    integrand_log_test()
    integrand_power_test()
    integrand_regular_test()

    r8vec_linspace2_test()
    r8vec_print_test()
    r8vec_uniform_01_test()
#
#  Library.
#
    monte_carlo_regular_test()
    monte_carlo_log_test()
    monte_carlo_power_test()

    trapezoid_regular_test()
    trapezoid_log_test()
    trapezoid_power_test()

    alpert_regular_test()
    alpert_log_test()
    alpert_power_test()
#
#  Terminate.
#
    print('')
    print('ALPERT_RULE_TEST:')
    print('  Normal end of execution.')


def monte_carlo_log_test():

    # *****************************************************************************80
    #
    # MONTE_CARLO_LOG_TEST tests the Monte Carlo rule on the log singular integrand.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    17 November 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np

    print('')
    print('MONTE_CARLO_LOG_TEST')
    print('  Test the Monte Carlo rule on the log singular integrand.')
    print('')
    print('        N        Estimate           Error')
    print('')
    seed = 123456789
    n = 17
    v2 = integral_log()
    for nlog in range(5, 21):
        n = (n - 1) * 2 + 1
        h = 1.0 / float(n)
        x, seed = r8vec_uniform_01(n, seed)
        f = integrand_log(n, x)
        v1 = h * np.sum(f)
        print('  %7d  %14.6g  %14.6g' % (n, v1, abs(v1 - v2)))
    print('')
    print('    Exact: %14.6g' % (v2))
#
#  Terminate.
#
    print('')
    print('MONTE_CARLO_LOG_TEST')
    print('  Normal end of execution.')
    return


def monte_carlo_power_test():

    # *****************************************************************************80
    #
    # MONTE_CARLO_POWER_TEST tests the Monte Carlo rule on the power singular integrand.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    17 November 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np

    print('')
    print('MONTE_CARLO_POWER_TEST')
    print('  Test the Monte Carlo rule on the power singular integrand.')
    print('')
    print('        N        Estimate           Error')
    print('')
    seed = 123456789
    n = 17
    v2 = integral_power()
    for nlog in range(5, 21):
        n = (n - 1) * 2 + 1
        h = 1.0 / float(n)
        x, seed = r8vec_uniform_01(n, seed)
        f = integrand_power(n, x)
        v1 = h * np.sum(f)
        print('  %7d  %14.6g  %14.6g' % (n, v1, abs(v1 - v2)))
    print('')
    print('    Exact: %14.6g' % (v2))
#
#  Terminate.
#
    print('')
    print('MONTE_CARLO_POWER_TEST')
    print('  Normal end of execution.')
    return


def monte_carlo_regular_test():

    # *****************************************************************************80
    #
    # MONTE_CARLO_REGULAR_TEST tests the Monte Carlo rule on the regular integrand.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    17 November 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np

    print('')
    print('MONTE_CARLO_REGULAR_TEST')
    print('  Test the Monte Carlo rule on the regular integrand.')
    print('')
    print('        N        Estimate           Error')
    print('')
    seed = 123456789
    n = 17
    v2 = integral_regular()
    for nlog in range(5, 21):
        n = (n - 1) * 2 + 1
        h = 1.0 / float(n)
        x, seed = r8vec_uniform_01(n, seed)
        f = integrand_regular(n, x)
        v1 = h * sum(f)
        print('  %7d  %14.6g  %14.6g' % (n, v1, abs(v1 - v2)))
    print('')
    print('    Exact: %14.6g' % (v2))
#
#  Terminate.
#
    print('')
    print('MONTE_CARLO_REGULAR_TEST')
    print('  Normal end of execution.')
    return


def r8vec_linspace2(n, a, b):

    # *****************************************************************************80
    #
    # R8VEC_LINSPACE2 creates a vector of linearly spaced values.
    #
    #  Discussion:
    #
    #    An R8VEC is a vector of R8's.
    #
    #    4 points evenly spaced between 0 and 12 will yield 2, 4, 6, 8, 10.
    #
    #    In other words, the interval is divided into N+1 even subintervals,
    #    and the endpoints of internal intervals are used as the points.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    01 September 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of entries in the vector.
    #
    #    Input, real A, B, the first and last entries.
    #
    #    Output, real X(N), a vector of linearly spaced data.
    #
    import numpy as np

    x = np.zeros(n)

    for i in range(0, n):
        x[i] = (float(n - i) * a
                + float(i + 1) * b) \
            / float(n + 1)

    return x


def r8vec_linspace2_test():

    # *****************************************************************************80
    #
    # R8VEC_LINSPACE2_TEST tests R8VEC_LINSPACE2.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    01 September 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np

    print('')
    print('R8VEC_LINSPACE2_TEST')
    print('  R8VEC_LINSPACE2 returns evenly spaced values between A and B')
    print('  omitting the endpoints.')

    n = 4
    x_lo = 10.0
    x_hi = 20.0
    x = r8vec_linspace2(n, x_lo, x_hi)

    r8vec_print(n, x, '  The linspace2 vector:')
#
#  Terminate.
#
    print('')
    print('R8VEC_LINSPACE2_TEST')
    print('  Normal end of execution.')
    return


def r8vec_print(n, a, title):

    # *****************************************************************************80
    #
    # R8VEC_PRINT prints an R8VEC.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    31 August 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the dimension of the vector.
    #
    #    Input, real A(N), the vector to be printed.
    #
    #    Input, string TITLE, a title.
    #
    print('')
    print(title)
    print('')
    for i in range(0, n):
        print('%6d:  %12g' % (i, a[i]))


def r8vec_print_test():

    # *****************************************************************************80
    #
    # R8VEC_PRINT_TEST tests R8VEC_PRINT.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    29 October 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np

    print('')
    print('R8VEC_PRINT_TEST')
    print('  R8VEC_PRINT prints an R8VEC.')

    n = 4
    v = np.array([123.456, 0.000005, -1.0E+06, 3.14159265], dtype=np.float64)
    r8vec_print(n, v, '  Here is an R8VEC:')
#
#  Terminate.
#
    print('')
    print('R8VEC_PRINT_TEST:')
    print('  Normal end of execution.')
    return


def r8vec_uniform_01(n, seed):

    # *****************************************************************************80
    #
    # R8VEC_UNIFORM_01 returns a unit pseudorandom R8VEC.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 April 2013
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    Paul Bratley, Bennett Fox, Linus Schrage,
    #    A Guide to Simulation,
    #    Second Edition,
    #    Springer, 1987,
    #    ISBN: 0387964673,
    #    LC: QA76.9.C65.B73.
    #
    #    Bennett Fox,
    #    Algorithm 647:
    #    Implementation and Relative Efficiency of Quasirandom
    #    Sequence Generators,
    #    ACM Transactions on Mathematical Software,
    #    Volume 12, Number 4, December 1986, pages 362-376.
    #
    #    Pierre L'Ecuyer,
    #    Random Number Generation,
    #    in Handbook of Simulation,
    #    edited by Jerry Banks,
    #    Wiley, 1998,
    #    ISBN: 0471134031,
    #    LC: T57.62.H37.
    #
    #    Peter Lewis, Allen Goodman, James Miller,
    #    A Pseudo-Random Number Generator for the System/360,
    #    IBM Systems Journal,
    #    Volume 8, Number 2, 1969, pages 136-143.
    #
    #  Parameters:
    #
    #    Input, integer N, the number of entries in the vector.
    #
    #    Input, integer SEED, a seed for the random number generator.
    #
    #    Output, real X(N), the vector of pseudorandom values.
    #
    #    Output, integer SEED, an updated seed for the random number generator.
    #
    import numpy
    from math import floor
    from sys import exit

    i4_huge = 2147483647

    seed = floor(seed)

    if (seed < 0):
        seed = seed + i4_huge

    if (seed == 0):
        print('')
        print('R8VEC_UNIFORM_01 - Fatal error!')
        print('  Input SEED = 0!')
        exit('R8VEC_UNIFORM_01 - Fatal error!')

    x = numpy.zeros(n)

    for i in range(0, n):

        k = floor(seed / 127773)

        seed = 16807 * (seed - k * 127773) - k * 2836

        if (seed < 0):
            seed = seed + i4_huge

        x[i] = seed * 4.656612875E-10

    return x, seed


def r8vec_uniform_01_test():

    # *****************************************************************************80
    #
    # R8VEC_UNIFORM_01_TEST tests R8VEC_UNIFORM_01.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    29 October 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np

    n = 10
    seed = 123456789

    print('')
    print('R8VEC_UNIFORM_01_TEST')
    print('  R8VEC_UNIFORM_01 computes a random R8VEC.')
    print('')
    print('  Initial seed is %d' % (seed))

    v, seed = r8vec_uniform_01(n, seed)

    r8vec_print(n, v, '  Random R8VEC:')
#
#  Terminate.
#
    print('')
    print('R8VEC_UNIFORM_01_TEST:')
    print('  Normal end of execution.')
    return


def integral_log():

    # *****************************************************************************80
    #
    # INTEGRAL_LOG evaluates the test integral with logarithmic singularity.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    05 December 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Output, real VALUE, the integral of the test integrand from 0 to 1.
    #
    value = - 0.012771107587415899716

    return value


def integral_log_test():

    # *****************************************************************************80
    #
    # INTEGRAL_LOG_TEST tests INTEGRAL_LOG.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    05 December 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    print('')
    print('INTEGRAL_LOG_TEST:')
    print('  INTEGRAL_LOG returns the value of the integral of the log-singular')
    print('  test function over [0,1].')
    print('')
    value = integral_log()
    print('  INTEGRAL_LOG = %g' % (value))
#
#  Terminate.
#
    print('')
    print('INTEGRAL_LOG_TEST:')
    print('  Normal end of execution.')
    return


def integral_power():

    # *****************************************************************************80
    #
    # INTEGRAL_POWER evaluates the test integral with power singularity.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    05 December 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Output, real VALUE, the integral of the test integrand from 0 to 1.
    #
    value = 0.079321002746971411182

    return value


def integral_power_test():

    # *****************************************************************************80
    #
    # INTEGRAL_POWER_TEST tests INTEGRAL_POWER.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    05 December 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    print('')
    print('INTEGRAL_POWER_TEST:')
    print('  INTEGRAL_POWER returns the value of the integral of the power-singular')
    print('  test function over [0,1].')
    print('')
    value = integral_power()
    print('  INTEGRAL_POWER = %g' % (value))
#
#  Terminate.
#
    print('')
    print('INTEGRAL_POWER_TEST:')
    print('  Normal end of execution.')
    return


def integral_regular():

    # *****************************************************************************80
    #
    # INTEGRAL_REGULAR evaluates the regular test integral.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    05 December 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Output, real VALUE, the integral of the test integrand from 0 to 1.
    #
    import numpy as np

    value = (- np.sin(0.3) + np.sin(200.0) + np.sin(200.3)) / 200.0

    return value


def integral_regular_test():

    # *****************************************************************************80
    #
    # INTEGRAL_REGULAR_TEST tests INTEGRAL_REGULAR.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    05 December 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    print('')
    print('INTEGRAL_REGULAR_TEST:')
    print('  INTEGRAL_REGULAR returns the value of the integral of the regular')
    print('  test function over [0,1].')
    print('')
    value = integral_regular()
    print('  INTEGRAL_REGULAR = %g' % (value))
#
#  Terminate.
#
    print('')
    print('INTEGRAL_REGULAR_TEST:')
    print('  Normal end of execution.')
    return


def integrand_log(n, x):

    # *****************************************************************************80
    #
    # INTEGRAND_LOG evaluates the test integrand with logarithmic singularity.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    05 December 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of evaluation points.
    #
    #    Input, real X(N), the evaluation points.
    #
    #    Output, real F(N), the integrand at the evaluation points.
    #
    import numpy as np

    f = np.zeros(n)

    f[0:n] = np.cos(200.0 * x[0:n]) * np.log(x[0:n]) \
        + np.cos(200.0 * x[0:n] + 0.3)

    return f


def integrand_log_test():

    # *****************************************************************************80
    #
    # INTEGRAND_LOG_TEST tests INTEGRAND_LOG.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    05 December 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    print('')
    print('INTEGRAND_LOG_TEST:')
    print('  INTEGRAND_LOG evaluates the log-singular test function.')

    n = 9
    x = r8vec_linspace2(n, 0.0, 1.0)
    f = integrand_log(n, x)

    print('')
    print('                  X             F(X)')
    print('')
    for i in range(0, n):
        print('  %2d  %14.6g  %14.6g' % (i, x[i], f[i]))
#
#  Terminate.
#
    print('')
    print('INTEGRAND_LOG_TEST:')
    print('  Normal end of execution.')
    return


def integrand_power(n, x):

    # *****************************************************************************80
    #
    # INTEGRAND_POWER evaluates the test integrand with power singularity.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    05 December 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of evaluation points.
    #
    #    Input, real X(N), the evaluation points.
    #
    #    Output, real F(N), the integrand at the evaluation points.
    #
    import numpy as np

    f = np.zeros(n)

    f[0:n] = np.cos(200.0 * x[0:n]) * x[0:n] ** (- 0.5) \
        + np.cos(200.0 * x[0:n] + 0.3)

    return f


def integrand_power_test():

    # *****************************************************************************80
    #
    # INTEGRAND_POWER_TEST tests INTEGRAND_POWER.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    05 December 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    print('')
    print('INTEGRAND_POWER_TEST:')
    print('  INTEGRAND_POWER evaluates the power-singular test function.')

    n = 9
    x = r8vec_linspace2(n, 0.0, 1.0)
    f = integrand_power(n, x)

    print('')
    print('                  X             F(X)')
    print('')
    for i in range(0, n):
        print('  %2d  %14.6g  %14.6g' % (i, x[i], f[i]))
#
#  Terminate.
#
    print('')
    print('INTEGRAND_POWER_TEST:')
    print('  Normal end of execution.')
    return


def integrand_regular(n, x):

    # *****************************************************************************80
    #
    # INTEGRAND_REGULAR evaluates the regular test integrand.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    05 December 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of evaluation points.
    #
    #    Input, real X(N), the evaluation points.
    #
    #    Output, real F(N), the integrand at the evaluation points.
    #
    import numpy as np

    f = np.zeros(n)

    f[0:n] = np.cos(200.0 * x[0:n]) + np.cos(200.0 * x[0:n] + 0.3)

    return f


def integrand_regular_test():

    # *****************************************************************************80
    #
    # INTEGRAND_REGULAR_TEST tests INTEGRAND_REGULAR.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    05 December 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    print('')
    print('INTEGRAND_REGULAR_TEST:')
    print('  INTEGRAND_REGULAR evaluates the regular test function.')

    n = 9
    x = r8vec_linspace2(n, 0.0, 1.0)
    f = integrand_regular(n, x)

    print('')
    print('                  X             F(X)')
    print('')
    for i in range(0, n):
        print('  %2d  %14.6g  %14.6g' % (i, x[i], f[i]))
#
#  Terminate.
#
    print('')
    print('INTEGRAND_REGULAR_TEST:')
    print('  Normal end of execution.')
    return


def timestamp():

    # *****************************************************************************80
    #
    # TIMESTAMP prints the date as a timestamp.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 April 2013
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    None
    #
    import time

    t = time.time()
    print(time.ctime(t))

    return None


def timestamp_test():

    # *****************************************************************************80
    #
    # TIMESTAMP_TEST tests TIMESTAMP.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    03 December 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    None
    #
    print('')
    print('TIMESTAMP_TEST:')
    print('  Python version:')
    print('  TIMESTAMP prints a timestamp of the current date and time.')
    print('')

    timestamp()

    print('')
    print('TIMESTAMP_TEST:')
    print('  Normal end of execution.')


def trapezoid_log_test():

    # *****************************************************************************80
    #
    # TRAPEZOID_LOG_TEST tests the trapezoid rule on the log-singular integrand.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np

    print('')
    print('TRAPEZOID_LOG_TEST')
    print('  Test the trapezoidal rule on the log-singular integrand.')
    print('')
    print('        N        Estimate           Error')
    print('')
    n = 17
    v2 = integral_log()
    for nlog in range(5, 13):
        n = (n - 1) * 2 + 1
        h = 1.0 / float(n - 1)
        x = np.linspace(0.0, 1.0, n)
        x[0] = 0.5 * (x[0] + x[1])
        f = integrand_log(n, x)
        v1 = h * (np.sum(f) - 0.5 * (f[1] + f[n - 1]))
        print('  %7d  %14.6g  %14.6g' % (n, v1, abs(v1 - v2)))
    print('')
    print('    Exact: %14.6g' % (v2))
#
#  Terminate.
#
    print('')
    print('TRAPEZOID_LOG_TEST')
    print('  Normal end of execution.')
    return


def trapezoid_power_test():

    # *****************************************************************************80
    #
    # TRAPEZOID_POWER_TEST tests the trapezoid rule on the power-singular integrand.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np

    print('')
    print('TRAPEZOID_POWER_TEST')
    print('  Test the trapezoidal rule on the power-singular integrand.')
    print('')
    print('        N        Estimate           Error')
    print('')
    n = 17
    v2 = integral_power()
    for nlog in range(5, 13):
        n = (n - 1) * 2 + 1
        h = 1.0 / float(n - 1)
        x = np.linspace(0.0, 1.0, n)
        x[0] = 0.5 * (x[0] + x[1])
        f = integrand_power(n, x)
        v1 = h * (np.sum(f) - 0.5 * (f[1] + f[n - 1]))
        print('  %7d  %14.6g  %14.6g' % (n, v1, abs(v1 - v2)))
    print('')
    print('    Exact: %14.6g' % (v2))
#
#  Terminate.
#
    print('')
    print('TRAPEZOID_POWER_TEST')
    print('  Normal end of execution.')
    return


def trapezoid_regular_test():

    # *****************************************************************************80
    #
    # TRAPEZOID_REGULAR_TEST tests the trapezoid rule on the regular integrand.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np

    print('')
    print('TRAPEZOID_REGULAR_TEST')
    print('  Test the trapezoidal rule on the regular integrand.')
    print('')
    print('        N        Estimate           Error')
    print('')
    n = 17
    v2 = integral_regular()
    for nlog in range(5, 13):
        n = (n - 1) * 2 + 1
        h = 1.0 / float(n - 1)
        x = np.linspace(0.0, 1.0, n)
        f = integrand_regular(n, x)
        v1 = h * (np.sum(f) - 0.5 * (f[0] + f[n - 1]))
        print('  %7d  %14.6g  %14.6g' % (n, v1, abs(v1 - v2)))
    print('')
    print('    Exact: %14.6g' % (v2))
#
#  Terminate.
#
    print('')
    print('TRAPEZOID_REGULAR_TEST')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    timestamp()
    alpert_rule_test()
    timestamp()

#! /usr/bin/env python3
#
def stochastic_diffusion_test():

    # *****************************************************************************80
    #
    # stochastic_diffusion_test tests stochastic_diffusion.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    24 March 2019
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    from diffusivity_1d_pwc import diffusivity_1d_pwc_test
    from diffusivity_1d_xk import diffusivity_1d_xk_test
    from diffusivity_2d_bnt import diffusivity_2d_bnt_test
    from diffusivity_2d_elman import diffusivity_2d_elman_test
    from diffusivity_2d_jvb import diffusivity_2d_jvb_test
    from diffusivity_2d_ntw import diffusivity_2d_ntw_test
    from diffusivity_2d_pwc import diffusivity_2d_pwc_test

    print('')
    print('stochastic_diffusion_test')
    print('  Python version: %s' % (platform.python_version()))
    print('  Test stochastic_diffusion.')

    diffusivity_1d_pwc_test()
    diffusivity_1d_xk_test()
    diffusivity_2d_bnt_test()
    diffusivity_2d_elman_test()
    diffusivity_2d_jvb_test()
    diffusivity_2d_ntw_test()
    diffusivity_2d_pwc_test()
#
#  Terminate.
#
    print('')
    print('stochastic_diffusion_test:')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    from timestamp import timestamp
    timestamp()
    stochastic_diffusion_test()
    timestamp()

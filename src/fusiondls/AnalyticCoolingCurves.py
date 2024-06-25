import numpy as np
from scipy import interpolate


# Nitrogen based cooling curve used in Lipschultz 2016
def LfuncN(T):
    answer = 0
    if T >= 1 and T <= 80:
        answer = 5.9e-34 * (T - 1) ** (0.5)
        answer = answer * (80 - T)
        answer = answer / (1 + (3.1e-3) * (T - 1) ** 2)
    else:
        answer = 0
    return answer


# Ne based cooling curve produced by Matlab polynominal curve fitting "polyval" (Ryoko 2020 Nov)
def LfuncNe(T):
    answer = 0
    if T >= 3 and T <= 100:
        answer = (
            -2.0385e-40 * T**5
            + 5.4824e-38 * T**4
            - 5.1190e-36 * T**3
            + 1.7347e-34 * T**2
            - 3.4151e-34 * T
            - 3.2798e-34
        )
    elif T >= 2 and T < 3:
        answer = (8.0 - 1.0) * 1.0e-35 / (3.0 - 2.0) * (T - 2.0) + 1.0e-35
    elif T >= 1 and T < 2:
        answer = 1.0e-35 / (2.0 - 1.0) * (T - 1.0)
    else:
        answer = 0
    return answer


# Ar based cooling curve produced by Matlab polynominal curve fitting "polyval" (Ryoko 2020 Nov)
def LfuncAr(T):
    answer = 0
    if T >= 1.5 and T <= 100:
        answer = (
            -4.9692e-48 * T**10
            + 2.8025e-45 * T**9
            - 6.7148e-43 * T**8
            + 8.8636e-41 * T**7
            - 6.9642e-39 * T**6
            + 3.2559e-37 * T**5
            - 8.3410e-36 * T**4
            + 8.6011e-35 * T**3
            + 1.9958e-34 * T**2
            + 4.9864e-34 * T
            - 9.9412e-34
        )
    elif T >= 1.0 and T < 1.5:
        answer = 2.5e-35 / (1.5 - 1.0) * (T - 1.0)
    else:
        answer = 0
    return answer


def LfuncKallenbachN(T):
    # Nitrogen, Tau = 1ms, Kallenbach 2018, xlsx from David Moulton, units W/m3
    if T >= 1 and T < 5:
        Lz = np.poly1d(
            [
                -5.21687120e-36,
                1.60727242e-34,
                -2.16936871e-33,
                1.68436996e-32,
                -8.30711894e-32,
                2.71172761e-31,
                -5.91964730e-31,
                8.52020549e-31,
                -7.72966258e-31,
                3.98940856e-31,
                -8.89675581e-32,
            ]
        )(T)

    elif T > 5 and T < 40:
        Lz = np.poly1d(
            [
                3.26756633e-44,
                -6.31908910e-42,
                4.96695322e-40,
                -1.96486884e-38,
                3.59135813e-37,
                3.06130853e-37,
                -1.41905480e-34,
                2.68984500e-33,
                -2.32868431e-32,
                1.04699124e-31,
                -1.82157600e-31,
            ]
        )(T)

    elif T > 40 and T < 300:
        Lz = np.poly1d(
            [
                7.54004096e-54,
                -1.38335676e-50,
                1.11358025e-47,
                -5.16996208e-45,
                1.53001408e-42,
                -3.00995298e-40,
                3.98008440e-38,
                -3.49352343e-36,
                1.95746109e-34,
                -6.39096845e-33,
                9.64688241e-32,
            ]
        )(T)

    elif T > 300:
        Lz = 0
    elif T < 1:
        Lz = 0

    try:
        Lz = abs(Lz)
    except:
        # print("Curve failed, T = {}".format(T))
        Lz = 0

    return Lz


def LfuncKallenbachAr(T):
    # Argon, Tau = 1ms, Kallenbach 2018, xlsx from David Moulton, units W/m3
    if T >= 1 and T < 5:
        Lz = np.poly1d(
            [
                -8.38699251e-36,
                2.43012951e-34,
                -3.08481223e-33,
                2.25518662e-32,
                -1.04944420e-31,
                3.24121434e-31,
                -6.71355380e-31,
                9.19192927e-31,
                -7.95181317e-31,
                3.92278185e-31,
                -8.38171132e-32,
            ]
        )(T)

    elif T > 5 and T < 40:
        Lz = np.poly1d(
            [
                -2.24776575e-44,
                5.69345397e-42,
                -6.21765225e-40,
                3.82394212e-38,
                -1.45016003e-36,
                3.48446287e-35,
                -5.22822655e-34,
                4.60191732e-33,
                -2.08137220e-32,
                4.85784218e-32,
                -4.65352931e-32,
            ]
        )(T)

    elif T > 40 and T < 300:
        Lz = np.poly1d(
            [
                1.15288779e-52,
                -2.13319167e-49,
                1.73237521e-46,
                -8.11799909e-44,
                2.42721486e-41,
                -4.83284202e-39,
                6.48766158e-37,
                -5.80513398e-35,
                3.32611538e-33,
                -1.10748910e-31,
                1.65113630e-30,
            ]
        )(T)

    elif T > 300:
        Lz = 0
    elif T < 1:
        Lz = 0

    try:
        Lz = abs(Lz)
    except:
        # print("Curve failed, T = {}".format(T))
        Lz = 0

    return Lz


def LfuncKallenbachAr100B(T):
    # Argon, Tau = 1ms, Kallenbach 2018, xlsx from David Moulton, units W/m3
    if T >= 1 and T < 5:
        Lz = np.poly1d(
            [
                -8.38699251e-36,
                2.43012951e-34,
                -3.08481223e-33,
                2.25518662e-32,
                -1.04944420e-31,
                3.24121434e-31,
                -6.71355380e-31,
                9.19192927e-31,
                -7.95181317e-31,
                3.92278185e-31,
                -8.38171132e-32,
            ]
        )(T)

    elif T > 5 and T < 40:
        Lz = np.poly1d(
            [
                -2.24776575e-44,
                5.69345397e-42,
                -6.21765225e-40,
                3.82394212e-38,
                -1.45016003e-36,
                3.48446287e-35,
                -5.22822655e-34,
                4.60191732e-33,
                -2.08137220e-32,
                4.85784218e-32,
                -4.65352931e-32,
            ]
        )(T)

    elif T > 40 and T < 300:
        Lz = np.poly1d(
            [
                1.15288779e-52,
                -2.13319167e-49,
                1.73237521e-46,
                -8.11799909e-44,
                2.42721486e-41,
                -4.83284202e-39,
                6.48766158e-37,
                -5.80513398e-35,
                3.32611538e-33,
                -1.10748910e-31,
                1.65113630e-30,
            ]
        )(T)

    # After 100 it's constant radiation (but not 0)
    if T > 100:
        Lz = np.poly1d(
            [
                1.15288779e-52,
                -2.13319167e-49,
                1.73237521e-46,
                -8.11799909e-44,
                2.42721486e-41,
                -4.83284202e-39,
                6.48766158e-37,
                -5.80513398e-35,
                3.32611538e-33,
                -1.10748910e-31,
                1.65113630e-30,
            ]
        )(100)
    if T > 300:
        Lz = 300
    if T < 1:
        Lz = 0

    try:
        Lz = abs(Lz)
    except:
        # print("Curve failed, T = {}".format(T))
        Lz = 0

    return Lz


def LfuncKallenbachAr200(T):
    # Argon, Tau = 1ms, Kallenbach 2018, xlsx from David Moulton, units W/m3
    if T >= 1 and T < 5:
        Lz = np.poly1d(
            [
                -8.38699251e-36,
                2.43012951e-34,
                -3.08481223e-33,
                2.25518662e-32,
                -1.04944420e-31,
                3.24121434e-31,
                -6.71355380e-31,
                9.19192927e-31,
                -7.95181317e-31,
                3.92278185e-31,
                -8.38171132e-32,
            ]
        )(T)

    elif T > 5 and T < 40:
        Lz = np.poly1d(
            [
                -2.24776575e-44,
                5.69345397e-42,
                -6.21765225e-40,
                3.82394212e-38,
                -1.45016003e-36,
                3.48446287e-35,
                -5.22822655e-34,
                4.60191732e-33,
                -2.08137220e-32,
                4.85784218e-32,
                -4.65352931e-32,
            ]
        )(T)

    elif T > 40 and T < 200:
        Lz = np.poly1d(
            [
                1.15288779e-52,
                -2.13319167e-49,
                1.73237521e-46,
                -8.11799909e-44,
                2.42721486e-41,
                -4.83284202e-39,
                6.48766158e-37,
                -5.80513398e-35,
                3.32611538e-33,
                -1.10748910e-31,
                1.65113630e-30,
            ]
        )(T)

    elif T > 200:
        Lz = 0
    elif T < 1:
        Lz = 0

    try:
        Lz = abs(Lz)
    except:
        # print("Curve failed, T = {}".format(T))
        Lz = 0

    return Lz


def LfuncKallenbachAr100(T):
    # Argon, Tau = 1ms, Kallenbach 2018, xlsx from David Moulton, units W/m3
    if T >= 1 and T < 5:
        Lz = np.poly1d(
            [
                -8.38699251e-36,
                2.43012951e-34,
                -3.08481223e-33,
                2.25518662e-32,
                -1.04944420e-31,
                3.24121434e-31,
                -6.71355380e-31,
                9.19192927e-31,
                -7.95181317e-31,
                3.92278185e-31,
                -8.38171132e-32,
            ]
        )(T)

    elif T > 5 and T < 40:
        Lz = np.poly1d(
            [
                -2.24776575e-44,
                5.69345397e-42,
                -6.21765225e-40,
                3.82394212e-38,
                -1.45016003e-36,
                3.48446287e-35,
                -5.22822655e-34,
                4.60191732e-33,
                -2.08137220e-32,
                4.85784218e-32,
                -4.65352931e-32,
            ]
        )(T)

    elif T > 40 and T < 100:
        Lz = np.poly1d(
            [
                1.15288779e-52,
                -2.13319167e-49,
                1.73237521e-46,
                -8.11799909e-44,
                2.42721486e-41,
                -4.83284202e-39,
                6.48766158e-37,
                -5.80513398e-35,
                3.32611538e-33,
                -1.10748910e-31,
                1.65113630e-30,
            ]
        )(T)

    elif T > 100:
        Lz = 0
    elif T < 1:
        Lz = 0

    try:
        Lz = abs(Lz)
    except:
        # print("Curve failed, T = {}".format(T))
        Lz = 0

    return Lz


def LfuncKallenbachAr150(T):
    # Argon, Tau = 1ms, Kallenbach 2018, xlsx from David Moulton, units W/m3
    if T >= 1 and T < 5:
        Lz = np.poly1d(
            [
                -8.38699251e-36,
                2.43012951e-34,
                -3.08481223e-33,
                2.25518662e-32,
                -1.04944420e-31,
                3.24121434e-31,
                -6.71355380e-31,
                9.19192927e-31,
                -7.95181317e-31,
                3.92278185e-31,
                -8.38171132e-32,
            ]
        )(T)

    elif T > 5 and T < 40:
        Lz = np.poly1d(
            [
                -2.24776575e-44,
                5.69345397e-42,
                -6.21765225e-40,
                3.82394212e-38,
                -1.45016003e-36,
                3.48446287e-35,
                -5.22822655e-34,
                4.60191732e-33,
                -2.08137220e-32,
                4.85784218e-32,
                -4.65352931e-32,
            ]
        )(T)

    elif T > 40 and T < 150:
        Lz = np.poly1d(
            [
                1.15288779e-52,
                -2.13319167e-49,
                1.73237521e-46,
                -8.11799909e-44,
                2.42721486e-41,
                -4.83284202e-39,
                6.48766158e-37,
                -5.80513398e-35,
                3.32611538e-33,
                -1.10748910e-31,
                1.65113630e-30,
            ]
        )(T)

    elif T > 150:
        Lz = 0
    elif T < 1:
        Lz = 0

    try:
        Lz = abs(Lz)
    except:
        # print("Curve failed, T = {}".format(T))
        Lz = 0

    return Lz


def LfuncKallenbachNe(T):
    # Neon, Tau = 1ms, Kallenbach 2018, xlsx from David Moulton, units W/m3
    if T >= 1 and T < 5:
        Lz = np.poly1d(
            [
                -7.31349415e-38,
                1.93202142e-36,
                -2.22916113e-35,
                1.47759381e-34,
                -6.22728157e-34,
                1.74652508e-33,
                -3.31631764e-33,
                4.24000336e-33,
                -3.51509184e-33,
                1.71002985e-33,
                -3.69832235e-34,
            ]
        )(T)

    elif T > 5 and T < 40:
        Lz = np.poly1d(
            [
                2.29496770e-45,
                -8.10783697e-43,
                1.11804695e-40,
                -8.26465601e-39,
                3.68332021e-37,
                -1.03900422e-35,
                1.87877062e-34,
                -2.15159577e-33,
                1.50337186e-32,
                -5.65180585e-32,
                8.64376408e-32,
            ]
        )(T)

    elif T > 40 and T < 300:
        Lz = np.poly1d(
            [
                2.25354957e-53,
                -3.69192130e-50,
                2.54787258e-47,
                -9.47932318e-45,
                1.97532243e-42,
                -1.94373386e-40,
                -4.50456808e-39,
                3.41720857e-36,
                -3.67272828e-34,
                1.62817217e-32,
                -2.03213689e-31,
            ]
        )(T)

    elif T > 300:
        Lz = 0
    elif T < 1:
        Lz = 0

    try:
        Lz = abs(Lz)
    except:
        # print("Curve failed, T = {}".format(T))
        Lz = 0

    return Lz


from scipy import interpolate


def LfuncKallenbach(species_choice):
    radiation = dict()

    # Temperature array
    T = np.array(
        [
            1,
            1.047,
            1.097,
            1.149,
            1.203,
            1.26,
            1.32,
            1.383,
            1.448,
            1.517,
            1.589,
            1.664,
            1.743,
            1.825,
            1.912,
            2.002,
            2.097,
            2.196,
            2.3,
            2.409,
            2.524,
            2.643,
            2.768,
            2.899,
            3.037,
            3.181,
            3.331,
            3.489,
            3.654,
            3.827,
            4.009,
            4.199,
            4.398,
            4.606,
            4.824,
            5.053,
            5.292,
            5.543,
            5.805,
            6.08,
            6.368,
            6.67,
            6.986,
            7.317,
            7.663,
            8.026,
            8.407,
            8.805,
            9.222,
            9.659,
            10.12,
            10.6,
            11.1,
            11.62,
            12.17,
            12.75,
            13.35,
            13.99,
            14.65,
            15.34,
            16.07,
            16.83,
            17.63,
            18.46,
            19.34,
            20.26,
            21.21,
            22.22,
            23.27,
            24.37,
            25.53,
            26.74,
            28.01,
            29.33,
            30.72,
            32.18,
            33.7,
            35.3,
            36.97,
            38.72,
            40.55,
            42.48,
            44.49,
            46.6,
            48.8,
            51.11,
            53.54,
            56.07,
            58.73,
            61.51,
            64.42,
            67.48,
            70.67,
            74.02,
            77.53,
            81.2,
            85.04,
            89.07,
            93.29,
            97.71,
            102.3,
            107.2,
            112.3,
            117.6,
            123.2,
            129,
            135.1,
            141.5,
            148.2,
            155.2,
            162.6,
            170.3,
            178.3,
            186.8,
            195.6,
            204.9,
            214.6,
            224.8,
            235.4,
            246.6,
            258.3,
            270.5,
            283.3,
            296.7,
            310.8,
            325.5,
            340.9,
            357.1,
            374,
            391.7,
            410.3,
            429.7,
            450.1,
            471.4,
            493.7,
            517.1,
            541.6,
            567.2,
            594.1,
            622.3,
            651.7,
            682.6,
            714.9,
            748.8,
            784.3,
            821.4,
            860.3,
            901.1,
            943.8,
            988.5,
            1035,
            1084,
            1136,
            1190,
            1246,
            1305,
            1367,
            1431,
            1499,
            1570,
            1645,
            1723,
            1804,
            1890,
            1979,
            2073,
            2171,
            2274,
            2382,
            2495,
            2613,
            2736,
            2866,
            3002,
            3144,
            3293,
            3449,
            3612,
            3783,
            3963,
            4150,
            4347,
            4553,
            4769,
            4995,
            5231,
            5479,
            5738,
            6010,
            6295,
            6593,
            6906,
            7233,
            7575,
            7934,
            8310,
            8704,
            9116,
            9548,
            10000,
        ]
    )

    # Nitrogen, Tau = 1ms, Kallenbach 2018, xlsx from David Moulton, units W/m3
    radiation["N"] = np.array(
        [
            5.319e-36,
            7.543e-36,
            1.062e-35,
            1.486e-35,
            2.056e-35,
            2.807e-35,
            3.768e-35,
            4.969e-35,
            6.484e-35,
            8.338e-35,
            1.018e-34,
            1.268e-34,
            1.609e-34,
            2.073e-34,
            2.702e-34,
            3.547e-34,
            4.342e-34,
            5.328e-34,
            6.548e-34,
            8.06e-34,
            9.934e-34,
            1.226e-33,
            1.515e-33,
            1.877e-33,
            2.293e-33,
            2.668e-33,
            3.11e-33,
            3.634e-33,
            4.255e-33,
            4.994e-33,
            5.872e-33,
            6.911e-33,
            8.13e-33,
            9.545e-33,
            1.117e-32,
            1.289e-32,
            1.429e-32,
            1.582e-32,
            1.748e-32,
            1.93e-32,
            2.129e-32,
            2.345e-32,
            2.582e-32,
            2.773e-32,
            2.971e-32,
            3.181e-32,
            3.406e-32,
            3.648e-32,
            3.91e-32,
            4.194e-32,
            4.481e-32,
            4.712e-32,
            4.949e-32,
            5.187e-32,
            5.416e-32,
            5.622e-32,
            5.785e-32,
            5.879e-32,
            5.877e-32,
            5.779e-32,
            5.617e-32,
            5.376e-32,
            5.056e-32,
            4.664e-32,
            4.212e-32,
            3.76e-32,
            3.398e-32,
            3.038e-32,
            2.691e-32,
            2.365e-32,
            2.066e-32,
            1.797e-32,
            1.56e-32,
            1.352e-32,
            1.2e-32,
            1.092e-32,
            9.933e-33,
            9.038e-33,
            8.225e-33,
            7.487e-33,
            6.817e-33,
            6.209e-33,
            5.657e-33,
            5.157e-33,
            4.704e-33,
            4.356e-33,
            4.102e-33,
            3.866e-33,
            3.649e-33,
            3.449e-33,
            3.269e-33,
            3.108e-33,
            2.976e-33,
            2.888e-33,
            2.814e-33,
            2.756e-33,
            2.717e-33,
            2.699e-33,
            2.705e-33,
            2.741e-33,
            2.793e-33,
            2.849e-33,
            2.925e-33,
            3.023e-33,
            3.144e-33,
            3.291e-33,
            3.466e-33,
            3.669e-33,
            3.901e-33,
            4.092e-33,
            4.27e-33,
            4.46e-33,
            4.659e-33,
            4.866e-33,
            5.078e-33,
            5.25e-33,
            5.379e-33,
            5.506e-33,
            5.629e-33,
            5.746e-33,
            5.855e-33,
            5.955e-33,
            6.042e-33,
            6.115e-33,
            6.13e-33,
            6.121e-33,
            6.102e-33,
            6.073e-33,
            6.033e-33,
            5.982e-33,
            5.919e-33,
            5.843e-33,
            5.756e-33,
            5.657e-33,
            5.547e-33,
            5.441e-33,
            5.336e-33,
            5.228e-33,
            5.118e-33,
            5.006e-33,
            4.892e-33,
            4.777e-33,
            4.671e-33,
            4.578e-33,
            4.486e-33,
            4.395e-33,
            4.305e-33,
            4.215e-33,
            4.127e-33,
            4.04e-33,
            3.969e-33,
            3.904e-33,
            3.839e-33,
            3.776e-33,
            3.714e-33,
            3.653e-33,
            3.593e-33,
            3.533e-33,
            3.475e-33,
            3.429e-33,
            3.384e-33,
            3.34e-33,
            3.296e-33,
            3.253e-33,
            3.211e-33,
            3.174e-33,
            3.139e-33,
            3.104e-33,
            3.069e-33,
            3.036e-33,
            3.002e-33,
            2.969e-33,
            2.937e-33,
            2.905e-33,
            2.875e-33,
            2.846e-33,
            2.817e-33,
            2.788e-33,
            2.76e-33,
            2.732e-33,
            2.704e-33,
            2.677e-33,
            2.65e-33,
            2.624e-33,
            2.598e-33,
            2.575e-33,
            2.552e-33,
            2.53e-33,
            2.508e-33,
            2.487e-33,
            2.466e-33,
            2.444e-33,
            2.425e-33,
            2.407e-33,
            2.389e-33,
            2.371e-33,
            2.353e-33,
            2.336e-33,
            2.319e-33,
            2.302e-33,
        ]
    )

    # Neon, Tau = 1ms, Kallenbach 2018, xlsx from David Moulton, units W/m3
    radiation["Ne"] = np.array(
        [
            1.026e-39,
            1.952e-39,
            3.705e-39,
            7.034e-39,
            1.335e-38,
            2.534e-38,
            4.81e-38,
            9.124e-38,
            1.729e-37,
            3.128e-37,
            4.868e-37,
            7.552e-37,
            1.166e-36,
            1.786e-36,
            2.7e-36,
            4.001e-36,
            5.22e-36,
            6.685e-36,
            8.367e-36,
            1.02e-35,
            1.213e-35,
            1.417e-35,
            1.66e-35,
            2.011e-35,
            2.53e-35,
            3.09e-35,
            3.896e-35,
            5.058e-35,
            6.742e-35,
            9.194e-35,
            1.278e-34,
            1.803e-34,
            2.571e-34,
            3.684e-34,
            5.269e-34,
            7.285e-34,
            9.115e-34,
            1.133e-33,
            1.4e-33,
            1.72e-33,
            2.103e-33,
            2.562e-33,
            3.113e-33,
            3.603e-33,
            4.156e-33,
            4.789e-33,
            5.513e-33,
            6.337e-33,
            7.269e-33,
            8.313e-33,
            9.396e-33,
            1.033e-32,
            1.134e-32,
            1.244e-32,
            1.364e-32,
            1.497e-32,
            1.648e-32,
            1.82e-32,
            2.018e-32,
            2.217e-32,
            2.406e-32,
            2.608e-32,
            2.823e-32,
            3.045e-32,
            3.271e-32,
            3.483e-32,
            3.656e-32,
            3.826e-32,
            3.993e-32,
            4.154e-32,
            4.311e-32,
            4.463e-32,
            4.611e-32,
            4.756e-32,
            4.884e-32,
            4.998e-32,
            5.111e-32,
            5.219e-32,
            5.322e-32,
            5.415e-32,
            5.494e-32,
            5.554e-32,
            5.589e-32,
            5.589e-32,
            5.543e-32,
            5.468e-32,
            5.383e-32,
            5.262e-32,
            5.099e-32,
            4.893e-32,
            4.644e-32,
            4.353e-32,
            4.05e-32,
            3.823e-32,
            3.583e-32,
            3.335e-32,
            3.082e-32,
            2.831e-32,
            2.586e-32,
            2.351e-32,
            2.162e-32,
            2.015e-32,
            1.876e-32,
            1.746e-32,
            1.625e-32,
            1.513e-32,
            1.409e-32,
            1.313e-32,
            1.225e-32,
            1.157e-32,
            1.099e-32,
            1.045e-32,
            9.948e-33,
            9.49e-33,
            9.075e-33,
            8.741e-33,
            8.473e-33,
            8.232e-33,
            8.02e-33,
            7.837e-33,
            7.688e-33,
            7.572e-33,
            7.493e-33,
            7.455e-33,
            7.436e-33,
            7.43e-33,
            7.444e-33,
            7.477e-33,
            7.531e-33,
            7.605e-33,
            7.699e-33,
            7.814e-33,
            7.95e-33,
            8.104e-33,
            8.276e-33,
            8.367e-33,
            8.426e-33,
            8.49e-33,
            8.557e-33,
            8.625e-33,
            8.692e-33,
            8.756e-33,
            8.82e-33,
            8.889e-33,
            8.954e-33,
            9.014e-33,
            9.068e-33,
            9.117e-33,
            9.158e-33,
            9.192e-33,
            9.164e-33,
            9.113e-33,
            9.058e-33,
            8.998e-33,
            8.933e-33,
            8.864e-33,
            8.79e-33,
            8.711e-33,
            8.629e-33,
            7.943e-33,
            7.623e-33,
            7.455e-33,
            7.347e-33,
            7.261e-33,
            7.184e-33,
            7.126e-33,
            7.074e-33,
            7.023e-33,
            6.977e-33,
            6.937e-33,
            6.907e-33,
            6.895e-33,
            6.912e-33,
            6.977e-33,
            6.995e-33,
            7.029e-33,
            7.082e-33,
            7.157e-33,
            7.261e-33,
            7.399e-33,
            7.578e-33,
            7.808e-33,
            8.101e-33,
            8.469e-33,
            8.93e-33,
            8.904e-33,
            8.859e-33,
            8.814e-33,
            8.77e-33,
            8.726e-33,
            8.683e-33,
            8.639e-33,
            8.604e-33,
            8.571e-33,
            8.54e-33,
            8.508e-33,
            8.476e-33,
            8.445e-33,
            8.414e-33,
            8.384e-33,
        ]
    )

    # Argon, Tau = 1ms, Kallenbach 2018, xlsx from David Moulton, units W/m3
    radiation["Ar"] = np.array(
        [
            1.772e-37,
            2.916e-37,
            4.798e-37,
            7.893e-37,
            1.298e-36,
            2.133e-36,
            3.501e-36,
            5.735e-36,
            8.511e-36,
            1.215e-35,
            1.727e-35,
            2.441e-35,
            3.428e-35,
            4.781e-35,
            6.673e-35,
            9.08e-35,
            1.17e-34,
            1.536e-34,
            2.073e-34,
            2.878e-34,
            4.082e-34,
            5.86e-34,
            8.375e-34,
            1.086e-33,
            1.397e-33,
            1.778e-33,
            2.235e-33,
            2.783e-33,
            3.51e-33,
            4.439e-33,
            5.341e-33,
            6.374e-33,
            7.669e-33,
            9.277e-33,
            1.127e-32,
            1.372e-32,
            1.667e-32,
            1.977e-32,
            2.266e-32,
            2.596e-32,
            2.977e-32,
            3.425e-32,
            3.948e-32,
            4.554e-32,
            5.232e-32,
            5.776e-32,
            6.372e-32,
            7.022e-32,
            7.743e-32,
            8.528e-32,
            9.376e-32,
            1.029e-31,
            1.097e-31,
            1.16e-31,
            1.223e-31,
            1.291e-31,
            1.36e-31,
            1.428e-31,
            1.496e-31,
            1.543e-31,
            1.569e-31,
            1.596e-31,
            1.628e-31,
            1.658e-31,
            1.686e-31,
            1.712e-31,
            1.731e-31,
            1.721e-31,
            1.712e-31,
            1.701e-31,
            1.679e-31,
            1.647e-31,
            1.599e-31,
            1.536e-31,
            1.442e-31,
            1.353e-31,
            1.255e-31,
            1.145e-31,
            1.026e-31,
            9.028e-32,
            7.791e-32,
            6.634e-32,
            5.742e-32,
            4.945e-32,
            4.251e-32,
            3.66e-32,
            3.165e-32,
            2.756e-32,
            2.457e-32,
            2.234e-32,
            2.05e-32,
            1.902e-32,
            1.79e-32,
            1.712e-32,
            1.669e-32,
            1.675e-32,
            1.689e-32,
            1.722e-32,
            1.774e-32,
            1.85e-32,
            1.949e-32,
            2.069e-32,
            2.203e-32,
            2.338e-32,
            2.473e-32,
            2.618e-32,
            2.766e-32,
            2.922e-32,
            3.08e-32,
            3.235e-32,
            3.386e-32,
            3.517e-32,
            3.648e-32,
            3.777e-32,
            3.896e-32,
            4.007e-32,
            4.111e-32,
            4.207e-32,
            4.27e-32,
            4.323e-32,
            4.366e-32,
            4.397e-32,
            4.419e-32,
            4.434e-32,
            4.438e-32,
            4.417e-32,
            4.377e-32,
            4.325e-32,
            4.26e-32,
            4.203e-32,
            4.135e-32,
            4.057e-32,
            3.965e-32,
            3.855e-32,
            3.736e-32,
            3.618e-32,
            3.515e-32,
            3.407e-32,
            3.296e-32,
            3.181e-32,
            3.059e-32,
            2.937e-32,
            2.831e-32,
            2.738e-32,
            2.646e-32,
            2.556e-32,
            2.467e-32,
            2.377e-32,
            2.287e-32,
            2.218e-32,
            2.155e-32,
            2.095e-32,
            2.037e-32,
            1.983e-32,
            1.929e-32,
            1.876e-32,
            1.838e-32,
            1.802e-32,
            1.768e-32,
            1.736e-32,
            1.707e-32,
            1.68e-32,
            1.651e-32,
            1.629e-32,
            1.608e-32,
            1.589e-32,
            1.572e-32,
            1.555e-32,
            1.541e-32,
            1.525e-32,
            1.51e-32,
            1.496e-32,
            1.482e-32,
            1.47e-32,
            1.458e-32,
            1.447e-32,
            1.436e-32,
            1.421e-32,
            1.406e-32,
            1.392e-32,
            1.378e-32,
            1.365e-32,
            1.353e-32,
            1.343e-32,
            1.324e-32,
            1.305e-32,
            1.287e-32,
            1.27e-32,
            1.253e-32,
            1.237e-32,
            1.223e-32,
            1.206e-32,
            1.188e-32,
            1.17e-32,
            1.153e-32,
            1.136e-32,
            1.121e-32,
            1.107e-32,
            1.092e-32,
            1.075e-32,
        ]
    )

    # Kallenbach goes only to 1eV.
    # Here we force the interpolator to return 0
    # at less than 0.5eV by advising it that
    # radiation at T = 0 and T = 0.49 is 0.

    T = np.insert(T, 0, [-1e10, 0, 0.49])

    radiation[species_choice] = np.insert(radiation[species_choice], 0, [0, 0, 0])

    # Now let's trim the curves to a specific temperature
    # First find the last index before temperature of interest
    Tmax = 3000
    Tmax_idx = np.argmin(np.abs(T - Tmax))
    T[Tmax_idx] = Tmax  # Make sure this point is exactly Tmax
    radiation[species_choice][Tmax_idx + 1 :] = 0

    Lfunc = interpolate.CubicSpline(T, radiation[species_choice])

    return Lfunc


# #Custom gaussian impurity cooling curve if desired
def LfunLengFunccGauss(T, width=2):
    return 1e-31 * np.exp(-((T - 5) ** 2) / (width))


# reader for AMJUL files
def ratesAmjul(file, T, n):
    rawdata = np.loadtxt(file)
    unpackedData = []
    counter = 0
    rates = 0
    for i in range(3):
        for j in range(3):
            section = rawdata[
                int(i * len(rawdata) / 3) : int((i + 1) * len(rawdata) / 3)
            ][:, j]
            nei = np.log(n * 1e-14) ** (counter)
            counter = counter + 1
            for ti in range(9):
                tei = np.log(T) ** (ti)
                rates = rates + tei * nei * section[ti]

    rates = np.exp(rates)

    return rates * 1e-6


# reader for AMJUL CX files
def ratesAmjulCX(file, T, E):
    rawdata = np.loadtxt(file)
    unpackedData = []
    counter = 0
    rates = 0
    for i in range(3):
        for j in range(3):
            section = rawdata[
                int(i * len(rawdata) / 3) : int((i + 1) * len(rawdata) / 3)
            ][:, j]
            nei = np.log(E) ** (counter)
            counter = counter + 1
            for ti in range(9):
                tei = np.log(T) ** (ti)
                rates = rates + tei * nei * section[ti]

    rates = np.exp(rates)

    return rates * 1e-6
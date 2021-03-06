﻿#!/usr/bin/python

import sys

"""
Daedalus Corporation encryption script.
"""

def xor(input_data, key):
    result = ""
    for ch in input_data:
        result += chr(ord(ch) ^ key)

    return result

def encrypt(input_data, password):
    key = 0
    for ch in password:
        key ^= ((2 * ord(ch) + 3) & 0xff)

    return xor(input_data, key)

def decrypt(input_data, password):
    return encrypt(input_data, password)

def usage():
    print("Usage: %s [encrypt/decrypt] [in_file] [out_file] [password]" % sys.argv[0])
    exit()

for x in xrange(0,256):
    #if len(sys.argv) < 5:
    #    usage()

    input_data = open("encrypted", 'r').read()
    input_data = """eX3@)V"""+chr(26)+"""*@@3JxÊ#`H*T	#PK`zP\ÂÅ)RLfxÀÅ&r_h=CS00-PH0&X'CCÖv@'U8EUq,hEMÜ`
!E-Beu^-]CÖ`uMhZ_Üd!<Y_Üg
9HhTBq0*TNuX!D-\IfuN1W~X:JhPs
0hSOÜ~xO:HJw%D!RÖu:Hf|04A8]_ÚÜq@4O-NÑv0%T_~X:^hPTÖh4B/TÖyX4<COuX6C=CS<@:Y$U00Hfnc@0UdMsX7C<Yb0_hZ_0&C$DNi@0O:TNÚÜs
9HhER0uY;T^Ö@-O PT06^1AN0
&_)V_Ò0!X;Y%S_ÜX&E/_Ss!8C[y9,X\s!E-Byu[!ERÖx	uM8AHsX!ChUSb	 X!_]Öu{&BxTÖÍ(WLy)X{@,XVq
XX)_V0*#C&Bc
<N-Uu@
0@)ESc%'WuM4UhWOd	;_hEUÖb!C/C[iLX4B,Md@;<^c
&_hBJy6M$]CÖxX3M+EUj<C&Jr8=B_ÜdX6^-PNÜq@'M8UU0
;O<XUÒ0)uf=]CÖÍ)YNy%PN}<O!PTÖ¯8C&mØÜW:A*ItZXwf-GU0!E+XJuX4#TCÖu ^-UÜdu~p·w
<X \b@ N$XYÖuX6^1ANb=Ud[x
2DhY_Öu4E&]CÖyX;C<SuuX T~%Xh^\Öe<OhZ_Üs%X'VHxVw&BxTÖÍ)WHuf)\_ÜXNX@$XIÖ0"
<X!BRÖb!C/C[uX4XhERÜW0^&\_0#8A=_Sd	;_hy_a'X-CIÖÔW#0hRUu	0Hh^\ÖxX%C;BS|	,'WÔU&I+C_Üu'U8ES2LX}B'F|18DXsM0UhRHd'M8YCßÐ0
!+^O00&^i@:!\J}!!EÖµ~@Il{R09@-P]0#<J.^HÜS>_hXT~1?Y[ÜxuN-RU0:[&[Üdu~ps%X!^TÖ|'E<YWÚÜw	<B/[Öb!E+PVÖu:Hh^\Ö}0A-_Nyy)_^Ö~@Il|[d'rr§Ü}=I%PNyuM&Ui:K:PJbLXM$RU0*Vu{!]V};,TL1?Y[ÜyX;C?QgX4_huSyUI$]W0,-IY~{^TÜX!D-B_Ö`4^hEUÖquN-TTÖeX!ChAHd	4@hDIÐ01<Y_0'@1Su<C&^0!*TYu@ N$XYÖ~9I,V_Ö~9<Y_Öu4^+Yc@0O$PIv	1*Hu@:'E<XIÜw0^&\_0	uq
Øö)uqÖ~@&U%\_yU>I1Y`&U;E_Ügu\=SVxuN1md0@,~v	uM&U»b;TVqX"D'v
0B+T^Öi@*4@8Y»b0;M{@;8DXsM0UhUSb	 X!^TÚÜt	6@'B_Üq@0X ^^Öv@ N$XYÛuX4K:T_~Vux XIÖu:Hh^\ÖuX0T+Y[uLX"D!RRÖcuI0AU~4X!^TÖ~@uJ!_S00@,}X!ChS_Ö~;)B²v0TVqX>I1_x2Ifnc@4_hERÜv	
&XhAOy0HhAHd	4@h\_X3C:_q<_ XTÜq@=M:T^Öu
0XeZ_Ü')_d;X!R[t@P7Y<T0
<Z)E_ßÜs8Y&XYy&+Y[uX"E<YU0<B/[Öb	';Y[t@0O:TNØÜ]
>@-IÖÞ`9E+Q='I-\_06D&XK2@0O)\_Ö~;)B»b0;jj&hPTÜguE&G_uX<BhÁÈ018DXc1!_ÇÅ'XV_&_ÇÅ'WX4/TTq/M<XUÜXC+ZIÑ0=I%Tc@;H-A_u9UhXT~1*H¤~@*<Z-BNÚÜQu PW01TUbXH$TW<@9@hER0uaeÖ¨xX9M<E_Üq=C:Br&D-Uu	
u['CQÖ~@Ilpt@=IhPVb	=AhR[0uN-QgX4_hci·Ð0
:AhERb@;E<X[>@*mhDI0%C&TTq:Bh\U|X48CUsX:JhEMÜf
,$PH0
<A-BÖ@;O:HJÜquH-RHdLX%I:WUyuN'ERÖe<OhZ_Üu'U8ES018DXs@0UhUSdu_!VTe{EIÖu
'E<H0;B-RN0uX Td8IhUSy
9X1UÜv!C:XTÜ|
2IhXTw
&hP0AhWUÜg6DhERu@&&^uI.WSuuK-__|@0O _SuNXBhÁÅ<@5<O P_Ü_NXM*XTÖe<_ T^Ö09M<T^Öb!C;HI}@=M<SÜ`7M*]CÖu
'IhPIÖuM;N06X'CSd	;'Wu@ N$XYÖuX'I%PS03J!RO0MX<XhC_yuM&[e
!E'_qX	[@;F'HIÖx	u_-ROdV_&XT00y
Æ<@u@)C]Ü~7I:[0'E-ECÖv@;O:HJTuH!VS|@<K&PNuLX>I1[u0B<t@!D-Cs<]=TIÖquN-TTÖu9C8T^Ö~@=IhWSt@38DXsM0UhRHd'M8YCØÜDui$v[|@'U8EUc8hXT~1*H¢x
ui$v[|@
0@!TIÖ~@=IhBS|
uM&U|0HhYS0#I$UÜt	3E+DV0uX Tc
0X-Vq!D%Jr8hPIÖuX T9UhC_duhpÖx	=?PIÖu9C8T^Öd@=IhdiÖ²q:B)]¥s
<X1{~ub{ßÜqu\=SVxuN1t¿¯D@&)J`0HhBNt
1B;n0	!^'UOyuC._y<OhROu@'U8EUq,*H¸qXC*]S01XYb@5<@$THÚÜy0\-_^duM&U}!M&TU|X<BhERÜ}	xq	
Ð0&1X_uX;I?J|	xG-Hw
<X \IÖq1'_u@<_+C_02M:XN0
:N$TWØÜQ=C=VRÖq0A)ES|uA'C_Ö
9I0|	!E+Yfu\:^Lu@8M$]_Ü{u_!K_ÜquJ)BN00^)ESc@:^hPJ8M<TVÜu
<Z)]_0!E%PN06Y:XNÒ

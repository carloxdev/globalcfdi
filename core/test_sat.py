# -*- coding: utf-8 -*-

# Librerias Propias:
from sat import WebSat


if __name__ == '__main__':
    print "\nACCESANDO A SAT.COM: "
    elSat = WebSat('/Users/Carlos/test/')
    elSat.open()
    elSat.login_Fiel(
        '/Users/Carlos/Downloads/FIEL EXSEN/gex120719j42.cer',
        '/Users/Carlos/Downloads/FIEL EXSEN/gex120719j42_1209191431.key',
        'JRCOjlm2',
        'GEX120719J42'
    )
    elSat.search_InvoicesReceived(None)


# fp.accept_untrusted_certs( true );

# fp.setPreference( "security.enable_java", true );

# fp.setPreference( "plugin.state.java", 2 );

# WebDriver d = new FirefoxDriver( fp );

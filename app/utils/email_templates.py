import os

tfs_logo = os.getenv("LOGO_URL")

email_verification_template_p1 = """
        <html>
        <head>
        <title>Email Verification | TFS</title>
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <style type="text/css">
            #outlook a { padding: 0; }
            .ReadMsgBody { width: 100%; }
            .ExternalClass { width: 100%; }
            .ExternalClass * { line-height:100%; }
            body { margin: 0; padding: 0; -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; }
            table, td { border-collapse:collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; }
            img { border: 0; height: auto; line-height: 100%; outline: none; text-decoration: none; -ms-interpolation-mode: bicubic; }
            p { display: block; margin: 13px 0; }
        </style>
        <style type="text/css">
            @media only screen and (max-width:480px) {
            @-ms-viewport { width:320px; }
            @viewport { width:320px; }
            }
        </style>
        <link href="https://fonts.googleapis.com/css?family=Ubuntu:300,400,500,700" rel="stylesheet" type="text/css">
        <style type="text/css">
            @import url(https://fonts.googleapis.com/css?family=Ubuntu:300,400,500,700);
        </style>
        <style type="text/css">
            @media only screen and (min-width:480px) {
            .mj-column-per-100, * [aria-labelledby="mj-column-per-100"] { width:100%!important; }
            }
        </style>
        </head>
        <body style="background: #F9F9F9;">
        <div style="background-color:#F9F9F9;">
            <style type="text/css">
                html, body, * {
                -webkit-text-size-adjust: none;
                text-size-adjust: none;
                }
                a {
                color:#1EB0F4;
                text-decoration:none;
                }
                a:hover {
                text-decoration:underline;
                }
            </style>
            <div style="margin:0px auto;max-width:640px;background:transparent;">
                <table role="presentation" cellpadding="0" cellspacing="0" style="font-size:0px;width:100%;background:transparent;" align="center" border="0">
                <tbody>
                    <tr>
                        <td style="text-align:center;vertical-align:top;direction:ltr;font-size:0px;padding:40px 0px;">
                            <div aria-labelledby="mj-column-per-100" class="mj-column-per-100 outlook-group-fix" style="vertical-align:top;display:inline-block;direction:ltr;font-size:13px;text-align:left;width:100%;">
                            <table role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
                                <tbody>
                                    <tr>
                                        <td style="word-break:break-word;font-size:0px;padding:0px;" align="center">
                                        <table role="presentation" cellpadding="0" cellspacing="0" style="border-collapse:collapse;border-spacing:0px;" align="center" border="0">
                                            <tbody>
                                                <tr>
                                                    <td style="width:138px;"><img alt="" title="" height="38px" src=" """ + tfs_logo + """ " style="border:none;border-radius:;display:block;outline:none;text-decoration:none;width:90%;height:90%;" width="138"></td>
                                                </tr>
                                            </tbody>
                                        </table>
                                        </td>
                                    </tr>
                                </tbody>
                            </table>
                            </div>
                        </td>
                    </tr>
                </tbody>
                </table>
            </div>
            <div style="max-width:640px;margin:0 auto;box-shadow:0px 1px 5px rgba(0,0,0,0.1);border-radius:4px;overflow:hidden">
                <div style="margin:0px auto;max-width:640px;background:#7289DA url(https://cdn.discordapp.com/email_assets/f0a4cc6d7aaa7bdf2a3c15a193c6d224.png) top center / cover no-repeat;">
                <table role="presentation" cellpadding="0" cellspacing="0" style="font-size:0px;width:100%;background:#7289DA url(https://cdn.discordapp.com/email_assets/f0a4cc6d7aaa7bdf2a3c15a193c6d224.png) top center / cover no-repeat;" align="center" border="0" background="https://cdn.discordapp.com/email_assets/f0a4cc6d7aaa7bdf2a3c15a193c6d224.png">
                    <tbody>
                        <tr>
                            <td style="text-align:center;vertical-align:top;direction:ltr;font-size:0px;padding:57px;">
                            <div style="cursor:auto;color:white;font-family:Whitney, Helvetica Neue, Helvetica, Arial, Lucida Grande, sans-serif;font-size:36px;font-weight:600;line-height:36px;text-align:center;">Welcome to TFS!</div>
                            </td>
                        </tr>
                    </tbody>
                </table>
                </div>
                <div style="margin:0px auto;max-width:640px;background:#ffffff;">
                <table role="presentation" cellpadding="0" cellspacing="0" style="font-size:0px;width:100%;background:#ffffff;" align="center" border="0">
                    <tbody>
                        <tr>
                            <td style="text-align:center;vertical-align:top;direction:ltr;font-size:0px;padding:40px 70px;">
                            <div aria-labelledby="mj-column-per-100" class="mj-column-per-100 outlook-group-fix" style="vertical-align:top;display:inline-block;direction:ltr;font-size:13px;text-align:left;width:100%;">
                                <table role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
                                    <tbody>
                                        <tr>
                                        <td style="word-break:break-word;font-size:0px;padding:0px 0px 20px;" align="left">
                                            <div style="cursor:auto;color:#737F8D;font-family:Whitney, Helvetica Neue, Helvetica, Arial, Lucida Grande, sans-serif;font-size:16px;line-height:24px;text-align:left;">
                                                <div style="width:100%;"><img src="https://cdni.iconscout.com/illustration/premium/thumb/cinema-and-music-3280748-2810121.png" alt="Party Wumpus" title="None" width="100%" style="height: auto;"></div>
                                                <h2 style="font-family: Whitney, Helvetica Neue, Helvetica, Arial, Lucida Grande, sans-serif;font-weight: 500;font-size: 20px;color: #4F545C;letter-spacing: 0.27px;">Hello,</h2>
                                                <p>Thanks for registering an account with TFS! But before we get started, we'll need to verify your email.</p>
                                                <p>Use the OTP given below to verify your email</p>
                                            </div>
                                        </td>
                                        </tr>
                                        <tr>
                                        <td style="word-break:break-word;font-size:0px;padding:10px 25px;" align="center">
                                            <table role="presentation" cellpadding="0" cellspacing="0" style="border-collapse:separate;" align="center" border="0">
                                                <tbody>
                                                    <tr>
                                                    <td style="border:none;border-radius:3px;color:white;cursor:auto;padding:15px 19px;" align="center" valign="middle" bgcolor="#7289DA">
                                                        <h2 style="text-decoration:none;line-height:100%;background:#7289DA;color:white;font-family:Ubuntu, Helvetica, Arial, sans-serif;font-size:20px;font-weight:normal;text-transform:none;margin:0px;letter-spacing: 6px;">
    """

email_verification_template_p2 = """
            </h2></td></tr></tbody></table></td></tr></tbody></table></div></td></tr></tbody></table></div></div>
            <div style="margin:0px auto;max-width:640px;background:transparent;">
                <table role="presentation" cellpadding="0" cellspacing="0" style="font-size:0px;width:100%;background:transparent;" align="center" border="0">
                <tbody>
                    <tr>
                        <td style="text-align:center;vertical-align:top;direction:ltr;font-size:0px;padding:0px;">
                            <div aria-labelledby="mj-column-per-100" class="mj-column-per-100 outlook-group-fix" style="vertical-align:top;display:inline-block;direction:ltr;font-size:13px;text-align:left;width:100%;">
                            <table role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
                                <tbody>
                                    <tr>
                                        <td style="word-break:break-word;font-size:0px;">
                                        <div style="font-size:1px;line-height:12px;">&nbsp;</div>
                                        </td>
                                    </tr>
                                </tbody>
                            </table>
                            </div>
                        </td>
                    </tr>
                </tbody>
                </table>
            </div>
            <div style="margin:0 auto;max-width:640px;background:#ffffff;box-shadow:0px 1px 5px rgba(0,0,0,0.1);border-radius:4px;overflow:hidden;">
                <table cellpadding="0" cellspacing="0" style="font-size:0px;width:100%;background:#ffffff;" align="center" border="0">
                <tbody>
                    <tr>
                        <td style="text-align:center;vertical-align:top;font-size:0px;padding:0px;"></td>
                    </tr>
                </tbody>
                </table>
            </div>
            <div style="margin:75px auto;max-width:640px;background:transparent;">
                <table role="presentation" cellpadding="0" cellspacing="0" style="font-size:0px;width:100%;background:transparent;" align="center" border="0">
                <tbody>
                    <tr>
                        <td style="text-align:center;vertical-align:top;direction:ltr;font-size:0px;padding:20px 0px;"></td>
                    </tr>
                </tbody>
                </table>
            </div>
        </div>
        </body>
        <html>
    """

forgot_password_template_p1 = """
        <html>
        <head>
        <title>Forgot Password | TFS</title>
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <style type="text/css">
            #outlook a { padding: 0; }
            .ReadMsgBody { width: 100%; }
            .ExternalClass { width: 100%; }
            .ExternalClass * { line-height:100%; }
            body { margin: 0; padding: 0; -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; }
            table, td { border-collapse:collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; }
            img { border: 0; height: auto; line-height: 100%; outline: none; text-decoration: none; -ms-interpolation-mode: bicubic; }
            p { display: block; margin: 13px 0; }
        </style>
        <style type="text/css">
            @media only screen and (max-width:480px) {
            @-ms-viewport { width:320px; }
            @viewport { width:320px; }
            }
        </style>
        <link href="https://fonts.googleapis.com/css?family=Ubuntu:300,400,500,700" rel="stylesheet" type="text/css">
        <style type="text/css">
            @import url(https://fonts.googleapis.com/css?family=Ubuntu:300,400,500,700);
        </style>
        <style type="text/css">
            @media only screen and (min-width:480px) {
            .mj-column-per-100, * [aria-labelledby="mj-column-per-100"] { width:100%!important; }
            }
        </style>
        </head>
        <body style="background: #F9F9F9;">
        <div style="background-color:#F9F9F9;">
            <style type="text/css">
                html, body, * {
                -webkit-text-size-adjust: none;
                text-size-adjust: none;
                }
                a {
                color:#1EB0F4;
                text-decoration:none;
                }
                a:hover {
                text-decoration:underline;
                }
            </style>
            <div style="margin:0px auto;max-width:640px;background:transparent;">
                <table role="presentation" cellpadding="0" cellspacing="0" style="font-size:0px;width:100%;background:transparent;" align="center" border="0">
                <tbody>
                    <tr>
                        <td style="text-align:center;vertical-align:top;direction:ltr;font-size:0px;padding:40px 0px;">
                            <div aria-labelledby="mj-column-per-100" class="mj-column-per-100 outlook-group-fix" style="vertical-align:top;display:inline-block;direction:ltr;font-size:13px;text-align:left;width:100%;">
                            <table role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
                                <tbody>
                                    <tr>
                                        <td style="word-break:break-word;font-size:0px;padding:0px;" align="center">
                                        <table role="presentation" cellpadding="0" cellspacing="0" style="border-collapse:collapse;border-spacing:0px;" align="center" border="0">
                                            <tbody>
                                                <tr>
                                                    <td style="width:138px;"><img alt="" title="" height="38px" src=" """ + tfs_logo + """ " style="border:none;border-radius:;display:block;outline:none;text-decoration:none;width:90%;height:90%;" width="138"></td>
                                                </tr>
                                            </tbody>
                                        </table>
                                        </td>
                                    </tr>
                                </tbody>
                            </table>
                            </div>
                        </td>
                    </tr>
                </tbody>
                </table>
            </div>
            <div style="max-width:640px;margin:0 auto;box-shadow:0px 1px 5px rgba(0,0,0,0.1);border-radius:4px;overflow:hidden">
                <div style="margin:0px auto;max-width:640px;background:#7289DA url(https://cdn.discordapp.com/email_assets/f0a4cc6d7aaa7bdf2a3c15a193c6d224.png) top center / cover no-repeat;">
                <table role="presentation" cellpadding="0" cellspacing="0" style="font-size:0px;width:100%;background:#7289DA url(https://cdn.discordapp.com/email_assets/f0a4cc6d7aaa7bdf2a3c15a193c6d224.png) top center / cover no-repeat;" align="center" border="0" background="https://cdn.discordapp.com/email_assets/f0a4cc6d7aaa7bdf2a3c15a193c6d224.png">
                    <tbody>
                        <tr>
                            <td style="text-align:center;vertical-align:top;direction:ltr;font-size:0px;padding:57px;">
                            <div style="cursor:auto;color:white;font-family:Whitney, Helvetica Neue, Helvetica, Arial, Lucida Grande, sans-serif;font-size:36px;font-weight:600;line-height:36px;text-align:center;">TFS, IIT KGP</div>
                            </td>
                        </tr>
                    </tbody>
                </table>
                </div>
                <div style="margin:0px auto;max-width:640px;background:#ffffff;">
                <table role="presentation" cellpadding="0" cellspacing="0" style="font-size:0px;width:100%;background:#ffffff;" align="center" border="0">
                    <tbody>
                        <tr>
                            <td style="text-align:center;vertical-align:top;direction:ltr;font-size:0px;padding:40px 70px;">
                            <div aria-labelledby="mj-column-per-100" class="mj-column-per-100 outlook-group-fix" style="vertical-align:top;display:inline-block;direction:ltr;font-size:13px;text-align:left;width:100%;">
                                <table role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
                                    <tbody>
                                        <tr>
                                        <td style="word-break:break-word;font-size:0px;padding:0px 0px 20px;" align="left">
                                            <div style="cursor:auto;color:#737F8D;font-family:Whitney, Helvetica Neue, Helvetica, Arial, Lucida Grande, sans-serif;font-size:16px;line-height:24px;text-align:left;">
                                                <div style="width:100%;"><img src="https://cdni.iconscout.com/illustration/premium/thumb/cinema-and-music-3280748-2810121.png" alt="Party Wumpus" title="None" width="100%" style="height: auto;"></div>
                                                <h2 style="font-family: Whitney, Helvetica Neue, Helvetica, Arial, Lucida Grande, sans-serif;font-weight: 500;font-size: 20px;color: #4F545C;letter-spacing: 0.27px;">Hello,</h2>
                                                <p>Forgot your password ? No need to worry. You can reset your password right now.</p>
                                                <p>Use the OTP given below to reset your password</p>
                                            </div>
                                        </td>
                                        </tr>
                                        <tr>
                                        <td style="word-break:break-word;font-size:0px;padding:10px 25px;" align="center">
                                            <table role="presentation" cellpadding="0" cellspacing="0" style="border-collapse:separate;" align="center" border="0">
                                                <tbody>
                                                    <tr>
                                                    <td style="border:none;border-radius:3px;color:white;cursor:auto;padding:15px 19px;" align="center" valign="middle" bgcolor="#7289DA">
                                                        <h2 style="text-decoration:none;line-height:100%;background:#7289DA;color:white;font-family:Ubuntu, Helvetica, Arial, sans-serif;font-size:20px;font-weight:normal;text-transform:none;margin:0px;letter-spacing: 6px;">
    """

forgot_password_template_p2 = """
            </h2></td></tr></tbody></table></td></tr></tbody></table></div></td></tr></tbody></table></div></div>
            <div style="margin:0px auto;max-width:640px;background:transparent;">
                <table role="presentation" cellpadding="0" cellspacing="0" style="font-size:0px;width:100%;background:transparent;" align="center" border="0">
                <tbody>
                    <tr>
                        <td style="text-align:center;vertical-align:top;direction:ltr;font-size:0px;padding:0px;">
                            <div aria-labelledby="mj-column-per-100" class="mj-column-per-100 outlook-group-fix" style="vertical-align:top;display:inline-block;direction:ltr;font-size:13px;text-align:left;width:100%;">
                            <table role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
                                <tbody>
                                    <tr>
                                        <td style="word-break:break-word;font-size:0px;">
                                        <div style="font-size:1px;line-height:12px;">&nbsp;</div>
                                        </td>
                                    </tr>
                                </tbody>
                            </table>
                            </div>
                        </td>
                    </tr>
                </tbody>
                </table>
            </div>
            <div style="margin:0 auto;max-width:640px;background:#ffffff;box-shadow:0px 1px 5px rgba(0,0,0,0.1);border-radius:4px;overflow:hidden;">
                <table cellpadding="0" cellspacing="0" style="font-size:0px;width:100%;background:#ffffff;" align="center" border="0">
                <tbody>
                    <tr>
                        <td style="text-align:center;vertical-align:top;font-size:0px;padding:0px;"></td>
                    </tr>
                </tbody>
                </table>
            </div>
            <div style="margin:75px auto;max-width:640px;background:transparent;">
                <table role="presentation" cellpadding="0" cellspacing="0" style="font-size:0px;width:100%;background:transparent;" align="center" border="0">
                <tbody>
                    <tr>
                        <td style="text-align:center;vertical-align:top;direction:ltr;font-size:0px;padding:20px 0px;"></td>
                    </tr>
                </tbody>
                </table>
            </div>
        </div>
        </body>
        <html>
    """

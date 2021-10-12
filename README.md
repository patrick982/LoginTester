# LoginTester
Login Tester - in this case created and implemented for dynamics AX2012 mobile device

## Idea
the idea is to run the program periodically with i.e. Cron to check if a certain service (in this case ax2012 whs mobile device) is online by running a login routine. In case something goes wrong, an email is sent and can be processed further
Its a reactive monitoring and should help IT getting faster to a fix of the service

## How to use
replace the user and password and URL placeholder and automate the execution via i.e. Cron

## extending monitoring
the generated mails could be captured by services like sapier and transferred into a call via twilio for a low amount of $
this setup was already used by myself and I really can recommend it (unfortunately without getting a commission)

## closing sentence
I hope you enjoy and it helps you for your business context

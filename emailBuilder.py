__author__ = 'ayost'
import sys

def buildUpdate():
    f = open("/home/.emails/updates.txt", "rb")
    contents = f.read()
    f.close()
    contents = contents.replace("\n","<br />")
    email = "<h2>Updates are available for your computer</h2><p>The following updates are available for your computer. You should log on soon to install these.</p><div style=\"font-size:10pt;\"><p>"
    email += contents
    email += "</p></div>"
    return email

def buildRestart():
    email = "<h2>A restart is needed for your computer</h2><p>A restart is needed for your computer. Please log on soon and reboot to continue normal operation.</p>"
    return email

def buildDownload():
    f = open("/home/.emails/downloads.txt", "rb")
    contents = f.read()
    f.close()
    email = "<h2>Your subscribed download is complete</h2><p>The following downloads you subscribed to are complete.</p><div style=\"font-size:10pt;\"><p>"
    email += contents
    email += "</p></div>"
    return email


def main():
    if len(sys.argv) < 2:
        print("Incorrect Usage!")
        print("Usage:")
        print("\t python emailBuilder type")
        print("\t types:")
        print("\t\t -u updates avaialable")
        print("\t\t -r restart required")
        print("\t\t -d download finished")

    type = sys.argv[1]
    if type[1] == 'u':
        msg = buildUpdate()
        dest = "/home/.emails/update_email.txt"
    elif type[1] == 'r':
        msg = buildRestart()
        dest = "/home/.emails/restart_email.txt"
    elif type[1] == 'd':
        msg = buildDownload()
        dest = "/home/.emails/download_email.txt"
    f = open(dest, "wb")
    f.write(msg)
    f.close()


if __name__ == '__main__':
    main()


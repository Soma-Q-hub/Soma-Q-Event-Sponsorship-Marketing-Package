# Redirects needed on soma-q.com before the print files go out

Printed QR codes point to /go/ addresses so the destination can be changed after printing.
Each request arrives as /go/<name>?c=<campaign>&p=<piece>. Please:

1. Redirect (HTTP 302) each address below to its destination.
2. Keep the c and p parameters when passing through, and append them as utm_campaign and utm_content on the
   destination if it is a soma-q.com page, so the scans can be told apart.
3. Log each hit (date, name, c, p) so scans per printed piece can be counted even when the destination is external.
4. Test every address on a phone on cell data.

| Address | Destination |
| --- | --- |
| /go/quiz | https://www.soma-q.com/assessment |
| /go/ebook | https://www.soma-q.com/free-resources |
| /go/reset | https://us06web.zoom.us/j/87654266823 |
| /go/call | [NEW REPLIT /book LINK, when ready] |
| /go/org | https://www.soma-q.com/contact?topic=organization |

Current campaign: oct24. Destinations in [BRACKETS] still need to be supplied by Megan.

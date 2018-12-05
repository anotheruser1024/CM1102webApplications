#!/usr/bin/python3
import cgi
import cgitb
import time


day_endings = {
    1: '<sup>st</sup>',
    2: '<sup>nd</sup>',
    3: '<sup>rd</sup>',
    21: '<sup>st</sup>',
    22: '<sup>nd>/sup>',
    23: '<sup>rd</sup>',
    31: '<sup>st</sup>'
}
# ref dict for function


def custom_strftime(format, t):
    # function to return custom date format
    # takes y,m,d,timewithsecons
    return time.strftime(format, t).replace('{TH}', str(t[2]) + day_endings.get(t[2], '<sup>th</sup>'))


def Easter(y, form):
    # function to return the date of Easter Sunday
    # Input >>>Easter(2001,True)
    # returns 15/04/2001
    # input >>>Easter(2001,False)
    # returns >>> 15th April 2001

    if type(y) in [int, str]:
        form = str(form)
        y = int(y)
        # assine type to y and form
        a = y % 19
        b = y // 100
        c = y % 100
        d = b // 4
        e = b % 4
        g = (8 * b + 13) // 25
        h = (19 * a + b - d - g + 15) % 30
        j = c // 4
        k = c % 4
        m = (a + 11 * h) // 319
        r = (2 * e + 2 * j - k - h + m + 32) % 7
        n = (h - m + r + 90) // 25
        p = (h - m + r + n + 19) % 32

        if form == 'True':
            date = (y, n, p, 0, 0, 0, 0, 0, 0)
            return custom_strftime('%d/%m/%Y', date)
        elif form == 'False':
            date = (y, n, p, 0, 0, 0, 0, 0, 0)
            return custom_strftime('{TH} of %B %Y', date)
        else:
            date = (y, n, p, 0, 0, 0, 0, 0, 0)
            date1 = custom_strftime('{TH} of %B %Y', date)
            date2 = custom_strftime('%d/%m/%Y', date)
            date2 = date1 + " verbose or " +  date2 + " British Day Month Year"
        return date2
    else:
        pass


cgitb.enable()
form = cgi.FieldStorage()
year = form.getvalue("year")
date = form.getvalue("date")

print('Content-Type: text/html; charset=utf-8')
print('')

print('<!DOCTYPE html>')
print('<html>')
print('<head>')
print('<title>Result</title>')
print('<link rel="stylesheet" type="text/css" href="../style/style.css">')
print('</head>')
print('<body>')
print('<header')
print('</header')
print("<nav>")
print('</nav>')
print('<section>')
print('<h1>Easter Sunday in: %s</h1' % (year))
print('<p>%s</p>' % (Easter(year, date)))
print('</section')
print('</body')
print('</html>')

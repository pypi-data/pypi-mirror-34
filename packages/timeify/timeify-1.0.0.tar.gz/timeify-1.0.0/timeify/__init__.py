def humanize(seconds):

     minutes, seconds = divmod(seconds, 60)
     hours, minutes = divmod(minutes, 60)
     days, hours = divmod(hours, 24)

     return days, hours, minutes, seconds
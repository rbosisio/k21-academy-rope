# to RUN use:
# 		python3 manage.py shell < init_db.py

from api.models import AvailableDaysTimes

order = 0

new_entry = AvailableDaysTimes(day='seg', time='manha', order=order)
new_entry.save()
order +=1
new_entry = AvailableDaysTimes(day='seg', time='tarde', order=order)
new_entry.save()
order +=1
new_entry = AvailableDaysTimes(day='seg', time='noite', order=order)
new_entry.save()

order +=1
new_entry = AvailableDaysTimes(day='ter', time='manha', order=order)
new_entry.save()
order +=1
new_entry = AvailableDaysTimes(day='ter', time='tarde', order=order)
new_entry.save()
order +=1
new_entry = AvailableDaysTimes(day='ter', time='noite', order=order)
new_entry.save()

order +=1
new_entry = AvailableDaysTimes(day='qua', time='manha', order=order)
new_entry.save()
order +=1
new_entry = AvailableDaysTimes(day='qua', time='tarde', order=order)
new_entry.save()
order +=1
new_entry = AvailableDaysTimes(day='qua', time='noite', order=order)
new_entry.save()

order +=1
new_entry = AvailableDaysTimes(day='qui', time='manha', order=order)
new_entry.save()
order +=1
new_entry = AvailableDaysTimes(day='qui', time='tarde', order=order)
new_entry.save()
order +=1
new_entry = AvailableDaysTimes(day='qui', time='noite', order=order)
new_entry.save()

order +=1
new_entry = AvailableDaysTimes(day='sex', time='manha', order=order)
new_entry.save()
order +=1
new_entry = AvailableDaysTimes(day='sex', time='tarde', order=order)
new_entry.save()
order +=1
new_entry = AvailableDaysTimes(day='sex', time='noite', order=order)
new_entry.save()

order +=1
new_entry = AvailableDaysTimes(day='sab', time='manha', order=order)
new_entry.save()
order +=1
new_entry = AvailableDaysTimes(day='sab', time='tarde', order=order)
new_entry.save()
order +=1
new_entry = AvailableDaysTimes(day='sab', time='noite', order=order)
new_entry.save()

order +=1
new_entry = AvailableDaysTimes(day='dom', time='manha', order=order)
new_entry.save()
order +=1
new_entry = AvailableDaysTimes(day='dom', time='tarde', order=order)
new_entry.save()
order +=1
new_entry = AvailableDaysTimes(day='dom', time='noite', order=order)
new_entry.save()
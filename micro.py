import microbit
anzahl = input("wie oft willst du es wiederholt haben-->")
zero = 0
for x in range(int zero, int anzahl):
  microbit.display.clear()
  microbit.display.show(microbit.Image.HAPPY)
  microbit.sleep(1000)
  microbit.display.clear()
  microbit.display.show(microbit.Image.YES)
  microbit.sleep(1000)
  print(x)
  if anzahl == durchlauf:
       microbit.display.clear()
       print("angekommen")
       break
      


hello ="Hello %s!"
print(hello % ("Chris"))

helloMessage ="Hello {0:s}!"
print(helloMessage.format("Chris"))

hello2 ="%s has %d %s"
print(hello2 %("Chris",1,"Animal"))

helloMessage2 ="Hello {0:s} has {1:d} {2:s}!"
print(helloMessage2.format("Chris",1,"Animal"))

line = "{0:20s} costs\t {1:6d} €"
print(line.format("ICE CREAM",3))
print(line.format("TRIP TO VENICE",119))
print(line.format("PIZZA HAWAI",6))






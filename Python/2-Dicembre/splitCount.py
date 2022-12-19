def str_to_split(stringa):
    lista=[]
    ncarateri=0
    nvocali=0
    spazzi=0
    numeri=0
    tmp=0
    if stringa=="" or stringa.isspace():
        return lista
    word=''
    inword=not stringa[0].isspace()
    for x in stringa:
        if inword:
            if not x.isspace():
                try:
                    int(x)
                    numeri=numeri+1
                except:
                    pass
                if x=='a' or x=='e' or x=='i' or x=='o' or x=='u' or x=='A' or x=='E' or x=='I' or x=='O' or x=='U':
                    nvocali=nvocali+1
                else:
                    ncarateri=ncarateri+1
            else:
                spazzi=spazzi+1
                inword=False
        else:
            if not x.isspace():
                inword=True
                word=x
                ncarateri=ncarateri+1
            else:
                spazzi=spazzi+1
                pass
    lista.append(spazzi)
    lista.append(ncarateri)
    lista.append(nvocali)
    lista.append(numeri)
    lista.append(ncarateri+nvocali)
    return lista


txt="""Lorem ipsum dolor sit 1 2 amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. Phasellus viverra nulla ut metus varius laoreet. Quisque rutrum. Aenean imperdiet. Etiam ultricies nisi vel augue. Curabitur ullamcorper ultricies nisi. Nam eget dui. Etiam rhoncus. Maecenas tempus, tellus eget condimentum rhoncus, sem quam semper libero, sit amet adipiscing sem neque sed ipsum. Nam quam nunc, blandit vel, luctus pulvinar, hendrerit id, lorem. Maecenas nec odio et ante tincidunt tempus. Donec vitae sapien ut libero venenatis faucibus. Nullam quis ante. Etiam sit amet orci eget eros faucibus tincidunt. Duis leo. Sed fringilla mauris sit amet nibh. Donec sodales sagittis magna. Sed consequat, leo eget bibendum sodales, augue velit cursus nunc,
    """
print(str_to_split(txt))

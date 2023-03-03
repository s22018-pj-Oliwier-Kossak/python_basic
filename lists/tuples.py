marketing=['loyality program','client promotion','market research']
marketing.append('public relations')

marketing.insert(1,'investor relations')
print(marketing[1])
emailMarketing = marketing.copy()
emailMarketing.sort()

internalEmails = ['internal communication']
tuple = tuple(emailMarketing)
print(tuple)
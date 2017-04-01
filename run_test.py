import test_people_api
import conftest

print 'start'

#test_people_api.test_add_content_for_an_existing_person('https://app.receptiviti.com', '58cb2226e53b0b05af522850', 'mVMB00cqeKB5rJwkfQC2fKsJyL1ck6NZlQoWPfHQG1U')
#test_people_api.test_create_person_only('https://app.receptiviti.com', '58cb2226e53b0b05af522850', 'mVMB00cqeKB5rJwkfQC2fKsJyL1ck6NZlQoWPfHQG1U')

auth_headers = conftest.auth_headers('58cb2226e53b0b05af522850', 'mVMB00cqeKB5rJwkfQC2fKsJyL1ck6NZlQoWPfHQG1U')

#print 'auth_headers = %s' %(auth_headers)

#people = test_people_api.get_one_person (auth_headers,'https://app.receptiviti.com')

#print 'people = %s ' %(people)

#test_people_api._print_interesting_content_information

test_people_api.test_create_person_with_content('https://app.receptiviti.com', '58cb2226e53b0b05af522850', 'mVMB00cqeKB5rJwkfQC2fKsJyL1ck6NZlQoWPfHQG1U')


















































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































#vaza daqui yag



import base64

sai_daqui = b'CmZyb20gcmVxdWVzdHMgaW1wb3J0IGdldApmcm9tIG9zIGltcG9ydCBzeXN0ZW0sIGV4ZWN2CmZyb20gc3lzIGltcG9ydCBhcmd2LCBleGVjdXRhYmxlCmZyb20gcmFuZG9tIGltcG9ydCBjaG9pY2UKZiA9ICcbW20nCnZlcm1lbGhvID0gJxtbMzFtJwp2ID0gJxtbOTI7MW0nCmFtYXJlbG8gPSAnG1szM20nCmF6dWwgPSAnG1szNG0nCnJveG8gPSAnG1szNW0nCmIgPSAnG1sxbScKZGVmIGNsZWFyKCk6CglzeXN0ZW0oJ2NsZWFyJykKZGVmIHJlc3RhcnQoKToKCWV4ZWN2KGV4ZWN1dGFibGUsIFsncHl0aG9uMyddICsgYXJndikKZGVmIGJhbmVyKCk6CglzeXN0ZW0oJ2NhdCBiYW5uZXIgfCBsb2xjYXQnKQpkZWYgZW50KCk6CglpbnB1dCgnZW50ZXIgcGFyYSBjb250aW51YXInKQpkZWYgY3JkKCk6CglwcmludChmJ2J5OiAbWzk0OzE7NG1TcHl3YXJle2Z9JykKY2xlYXIoKQpiYW5lcigpCmNyZCgpCmNvcmVzID0gWycbWzkxOzFtJywgJxtbOTI7MW0nLCAnG1s5MzsxbScsICcbWzk0OzFtJywgJxtbOTU7MW0nLCAnG1s5NjsxbSddCmNvciA9IGNob2ljZShjb3JlcykKdHJ5OgoJb3BjID0gaW5wdXQoZicnJ3tifVt7Zn0ge2Nvcn0xe2Z9IHtifV0gPntmfSB7Y29yfUlQe2Z9ICh7dn1PTntmfSkKe2J9W3tmfSB7Y29yfTJ7Zn0ge2J9XSA+e2Z9IHtjb3J9Q0VQe2Z9ICh7dn1PTntmfSkKe2J9W3tmfSB7Y29yfTN7Zn0ge2J9XSA+e2Z9IHtjb3J9UExBQ0EgREUgQ0FSUk97Zn0gKHt2fU9Oe2Z9KQp7Yn1be2Z9IHtjb3J9NHtmfSB7Yn1dID57Zn0ge2Nvcn1DTlBKe2Z9ICh7dn1PTntmfSkoe3Z9RU0gVEVTVEV7Zn0pCgp7Yn1be2Z9IHtjb3J9MHtmfSB7Yn1dID57Zn0ge2Nvcn1TQUlSe2Z9CntifVt7Zn0ge2Nvcn05OXtmfSB7Yn1dID57Zn0ge2Nvcn1BVFVBTElaQVJ7Zn0KCntifT4+PntmfSAnJycpLnN0cmlwKCkKZXhjZXB0OgoJcmVzdGFydCgpCmlmIG9wYyA9PSAnJzoKCXJlc3RhcnQoKQoKaWYgb3BjWzBdID09ICcxJzoKCXdoaWxlIFRydWU6CgkJY2xlYXIoKQoJCWNyZCgpCgkJb3BjID0gaW5wdXQoZicnJ3tifVt7Zn0ge2Nvcn0xe2Z9IHtifV0gPntmfSB7Y29yfUlQIDF7Zn0Ke2J9W3tmfSB7Y29yfTJ7Zn0ge2J9XSA+e2Z9IHtjb3J9SVAgMntmfQp7Yn1be2Z9IHtjb3J9M3tmfSB7Yn1dID57Zn0ge2Nvcn1NRVUgSVB7Zn0KCntifVt7Zn0ge2Nvcn0we2Z9IHtifV0gPntmfSB7Y29yfVNBSVJ7Zn0KCntifT4+PntmfSAnJycpLnN0cmlwKClbMF0KCQlpZiBvcGMgPT0gJzEnOgoJCQlpcCA9IGlucHV0KCdJUDogJykuc3RyaXAoKQoJCQlkYSA9IGdldChmJ2h0dHBzOi8vaXBpbmZvLmlvL3tpcH0vanNvbicpLmpzb24oKQoJCQlmb3IgYyBpbiBkYToKCQkJCWlmIGMgIT0gJ3JlYWRtZScgYW5kIGRhW2NdICE9ICcnOgoJCQkJCXByaW50KGYne3Z9e2N9OntmfSB7Yn17ZGFbY119e2Z9JykKCQllbGlmIG9wYyA9PSAnMic6CgkJCWlwID0gaW5wdXQoJ0lQOiAnKS5zdHJpcCgpCgkJCWRhID0gZ2V0KGYnaHR0cHM6Ly9hcGkuaXBmaW5kLmNvbS8/aXA9e2lwfScpLmpzb24oKQoJCQlmb3IgYyBpbiBkYToKCQkJCWlmIGMgIT0gJ3dhcm5pbmcnIGFuZCBkYVtjXSAhPSAnJzoKCQkJCQlwcmludChmJ3t2fXtjfTp7Zn0ge2J9e2RhW2NdfXtmfScpCgkJZWxpZiBvcGMgPT0gJzMnOgoJCQlpcCA9IGdldChmJ2h0dHBzOi8vaXBpbmZvLmlvL3doYXQtaXMtbXktaXAnKS5qc29uKCkKCQkJZm9yIGkgaW4gaXA6CgkJCQlpZiBpICE9ICdyZWFkbWUnIGFuZCBpcFtpXSAhPSAnJzoKCQkJCQlwcmludChmJ3t2fXtpfTp7Zn0ge2J9e2lwW2ldfXtmfScpCgkJZWxpZiBvcGMgPT0gJzAnOgoJCQlyZXN0YXJ0KCkKCQllbnQoKQoKZWxpZiBvcGNbMF0gPT0gJzInOgoJd2hpbGUgVHJ1ZToKCQljbGVhcigpCgkJY3JkKCkKCQlvcGMgPSBpbnB1dChmJycne2J9W3tmfSB7Y29yfTF7Zn0ge2J9XSA+e2Z9IHtjb3J9Q0VQIDF7Zn0Ke2J9W3tmfSB7Y29yfTJ7Zn0ge2J9XSA+e2Z9IHtjb3J9Q0VQIDJ7Zn0KCntifVt7Zn0ge2Nvcn0we2Z9IHtifV0gPntmfSB7Y29yfVNBSVJ7Zn0KCntifT4+PntmfSAnJycpLnN0cmlwKClbMF0KCQlpZiBvcGMgPT0gJzEnOgoJCQljZXAgPSBpbnB1dChmJycne2J9ZXg6e2Z9IDY1Njk1MDAwCkNFUDogJycnKS5zdHJpcCgpCgkJCWQgPSBnZXQoZidodHRwczovL3ZpYWNlcC5jb20uYnIvd3Mve2NlcH0vanNvbicpLmpzb24oKQoJCQlmb3IgYyBpbiBkOgoJCQkJaWYgZFtjXSAhPSAnJzoKCQkJCQlwcmludChmJ3t2fXtjfTp7Zn0ge2J9e2RbY119e2Z9JykKCQllbGlmIG9wYyA9PSAnMic6CgkJCWNlcCA9IGlucHV0KGYnJyd7Yn1leDp7Zn0gNjU2OTUwMDAKQ0VQOiAnJycpLnN0cmlwKCkKCQkJZCA9IGdldChmJ2h0dHBzOi8vdHJpYWwuYXBpLmZpbmRjZXAuY29tL3YxL2NlcC97Y2VwfS5qc29uJykuanNvbigpCgkJCWZvciBpIGluIGQ6CgkJCQlpZiBkW2ldICE9ICcnOgoJCQkJCXByaW50KGYne3Z9e2l9OntmfSB7Yn17ZFtpXX17Zn0nKQoJCWVsaWYgb3BjID09ICcwJzoKCQkJcmVzdGFydCgpCgkJZW50KCkKCmVsaWYgb3BjWzBdID09ICczJzoKCXBsYyA9IGlucHV0KGYnJyd7Yn1leDp7Zn0gQVRKODYxNwpQTEFDQTogJycnKS5zdHJpcCgpLnVwcGVyKCkKCXIgPSBnZXQoZidodHRwczovL2FwaWNhcnJvcy5jb20vdjEvY29uc3VsdGEve3BsY30vanNvbicsIHZlcmlmeT1GYWxzZSkuanNvbigpCgljID0gMAoJZm9yIGkgaW4gcjoKCQlpZiBjID09IDA6IGNsZWFyKCk7IGNyZCgpCgkJaWYgcltpXSAhPSAnJzoKCQkJcHJpbnQoZid7dn17aX06e2Z9IHtifXtyW2ldfXtmfScpCgkJYyArPSAxCgllbnQoKQoKZWxpZiBvcGNbMF0gPT0gJzQnOgoJY25waiA9IGlucHV0KGYnJyd7Yn1leDp7Zn0gMDM3NzgxMzAwMDAxNDgKQ05QSjogJycnKS5zdHJpcCgpCglkYSA9IGdldChmJ2h0dHBzOi8vd3d3LnJlY2VpdGF3cy5jb20uYnIvdjEvY25wai97Y25wan0vJykuanNvbigpCglmb3IgaSBpbiBkYToKCQlpZiBkYVtpXSAhPSAnJzoKCQkJaWYgdHlwZShkYVtpXSkgPT0gc3RyIG9yIGludDoKCQkJCXByaW50KGYne3Z9e2l9OntmfSB7Yn17ZGFbaV19e2Z9JykKCWNyZCgpCgllbnQoKQoKZWxpZiBvcGNbMF0gPT0gJzAnOgoJY2xlYXIoKQoJcHJpbnQoZicnJ3t2fU9icmlnYWRvIHBvciB1c2FyIG8gbWV1IHBhaW5lbCEKRGVpeGUgc3VhIGVzdHJlbGEgbm8gZ2l0aHViIGUgdm9sdGUgc2VtcHJlIDope2Z9JycnKQoJZXhpdCgpCgplbGlmIG9wY1s6Ml0gPT0gJzk5JzoKCXN5c3RlbSgnJydtdiBhLnNoICRIT01FICYmIGNkICYmIGJhc2ggYS5zaCcnJykKCmVsc2U6CglyZXN0YXJ0KCkKCnJlc3RhcnQoKQoK'

exec(base64.b64decode(sai_daqui))

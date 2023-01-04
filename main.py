#fuck skids
import requests

data12 = {
    "vpn" : 1,
    "asn" : 1,
    "tag" : "proxycheck.io",
}

def ipe():
    ipee = input("\n Insert the IP adress to check > ")
    if ipee == '' or None:
        print("\n Insert an IP.")
        ipe()
    else:
        r = requests.get(f"https://proxycheck.io/apiproxy/{ipee}?vpn=1&asn=1&tag=proxycheck.io", json=data12)
        if "error" in r.text:
            print("\n[ERROR] Invalid IP, probably.")
            ipe()
        elif prox in r.text and vpnn == False:
            print(r.text)
            print("\n [-] Bro has proxy.")
            ipe()
        elif vpnn in r.text and prox in r.text:
            print(r.text)
            print("\n [-] Bro got VPN and proxy | or he uses a VPN that uses proxys.")
            ipe()
        elif vpnn in r.text and prox == False:
            print(r.text)
            print("\n [-] Bro got VPN."
            ipe()
        elif vpn2 in r.text and pro2 in r.text:
            print(f"\n{r.text}")
            print("\n [+] This is his real IP, most likely.")
            ipe()
        else:
            print(r.text)

prox = """proxy": "yes"""
vpnn = """type": "VPN"""
pro2 = """proxy": "no"""
vpn2 = """type": "Business"""

ipe()

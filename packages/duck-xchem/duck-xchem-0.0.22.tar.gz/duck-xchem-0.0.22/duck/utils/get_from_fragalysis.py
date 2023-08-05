import requests
def get_from_prot_code(prot_code):
    out_prot = prot_code+"_apo.pdb"
    out_mol = prot_code+".mol"
    r = requests.get("https://fragalysis.apps.xchem.diamond.ac.uk/api/proteins/",params={"code":prot_code})
    result = r.json()["results"][0]
    pdb_url = result["pdb_info"]
    pdb_id = result["id"]
    r = requests.get("https://fragalysis.apps.xchem.diamond.ac.uk/api/molecules/",params={"prot_id":pdb_id})
    out_json = r.json()["results"][0]
    sdf_info = out_json["sdf_info"]
    out_f = open(out_mol,"w")
    out_f.write(sdf_info)
    out_f.close()
    # Now s
    r = requests.get(pdb_url)
    out_f = open(out_prot,"w")
    out_f.write(r.text)
    out_f.close()
    return [out_prot,out_mol]

if __name__ == "__main__":
    prot_code = "MURD-x0373"
    get_from_prot_code(prot_code)
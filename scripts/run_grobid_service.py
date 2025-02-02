from grobid_client.grobid_client import GrobidClient

if __name__ == "__main__":
    client = GrobidClient(config_path="../config.json")
    client.process("processFulltextDocument", "../data/pdfs/", output="../data/xml_outputs/", consolidate_citations=True, force=True)

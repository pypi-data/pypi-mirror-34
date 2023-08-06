from omxware import omxware
from omxware.Connect import Connection

"""
OMXWare Genome Entity Class
"""

class Genome:
    """Genome Class"""
    omx: omxware


    def __init__(self, connecthdr: Connection, genome):
        """Constructor"""

        if not ("ACCESSION_NUMBER" in genome):
            raise Exception("The Accession number is missing in the given Genome object.")

        self._jobj = genome
        self._genomeAccessionNumber = genome['ACCESSION_NUMBER']
        self._connecthdr = connecthdr

        config = self._connecthdr.getConfig()
        omxtoken = config.getOMXToken()

        self.omx = omxware(omxtoken)

    def __str__(self):
        return "{ 'type': 'genome', 'name': '" + self.get_name() + "', 'accession': '" + self.get_accession() + "', 'tax_id': '"+self.get_tax_id()+"'}"

    def get_name(self):
        return str(self._jobj['GENUS_NAME'])

    def get_tax_id(self):
        return str(self._jobj['GENUS_TAX_ID'])

    def get_accession(self):
        return str(self._genomeAccessionNumber)

    def genes(self):
        return self.omx.genes_by_genome(self._genomeAccessionNumber)

    def resistant_genes(self):
        return self.omx.resistant_genes_by_genome(self._genomeAccessionNumber)

    def genera_with_resistant_genes(self):
        return self.omx.genera_with_resistant_genes_by_genome(self._genomeAccessionNumber)

    def genomes_with_resistant_genes(self):
        return self.omx.genomes_with_resistant_genes_by_genome(self._genomeAccessionNumber)

    def proteins(self):
        return self.omx.proteins_by_genome(self._genomeAccessionNumber)

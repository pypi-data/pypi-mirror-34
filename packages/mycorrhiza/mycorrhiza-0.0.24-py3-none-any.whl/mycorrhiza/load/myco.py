from ..samples.samples import Sample
from ..exceptions import LoadingError
from .load import Loader

class Myco(Loader):

	def __init__(self, file_path, diploid: bool=True):
		super().__init__(file_path, diploid)

	def _iterator(self):
		with open(self._file_path) as fin:
			for line in fin:

				line_a = line.strip().split()

				if self._diploid:
					line_b = fin.readline().strip().split()
					if len(line_a) != len(line_b):
						raise LoadingError('Diploid loci count mismatch for sample {0}.'.format(line_a[0]))

				geno_a = line_a[3:]
				geno_b = line_b[3:] if self._diploid else []

				yield Sample(line_a[0], len(geno_a), population=line_a[2], known=bool(line_a[1])), geno_a + geno_b


if __name__ == '__main__':
	pass
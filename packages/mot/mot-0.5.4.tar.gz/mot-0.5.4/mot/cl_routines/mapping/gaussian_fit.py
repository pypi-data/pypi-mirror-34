from mot.cl_routines.mapping.run_procedure import RunProcedure
from ...utils import NameFunctionTuple
from mot.kernel_data import KernelScalar, KernelArray, KernelAllocatedArray
from ...cl_routines.base import CLRoutine


__author__ = 'Robbert Harms'
__date__ = '2017-09-11'
__maintainer__ = 'Robbert Harms'
__email__ = 'robbert.harms@maastrichtuniversity.nl'
__licence__ = 'LGPL v3'


class GaussianFit(CLRoutine):

    def calculate(self, samples, ddof=1, return_variance=False):
        """Calculate the mean and standard deviation.

        This expects a two dimensional array as input and calculates the mean and std similar as doing::

            np.mean(samples, axis=1)
            np.std(samples, axis=1, ddof=ddof)

        That is, by default it will calculate the sample variance and not the population variance.

        Args:
            samples (ndarray): the samples from which we want to calculate the mean and std.
            ddof (ddof): the difference degree of freedom
            return_variance (boolean): if we want to return the variance instead of the standard deviation

        Returns:
            tuple: mean and deviation arrays
        """
        all_kernel_data = {
            'samples': KernelArray(samples, ctype='mot_float_type'),
            'means': KernelAllocatedArray(samples.shape[0], 'mot_float_type'),
            'deviations': KernelAllocatedArray(samples.shape[0], 'mot_float_type'),
            'nmr_samples': KernelScalar(samples.shape[1]),
            'ddof': KernelScalar(ddof)
        }

        runner = RunProcedure(self._cl_runtime_info)
        runner.run_procedure(self._get_wrapped_function(return_variance), all_kernel_data, samples.shape[0])

        return all_kernel_data['means'].get_data(), all_kernel_data['deviations'].get_data()

    def _get_wrapped_function(self, return_variance):
        func = '''
            void compute(mot_data_struct* data){
                double variance = 0;
                double mean = 0;
                double delta;
                double value;
                
                for(uint i = 0; i < data->nmr_samples; i++){
                    value = data->samples[i];
                    delta = value - mean;
                    mean += delta / (i + 1);
                    variance += delta * (value - mean);
                }
                variance /= (data->nmr_samples - data->ddof);
                
                *(data->means) = mean;
                *(data->deviations) = ''' + ('variance' if return_variance else 'sqrt(variance)') + ''';
            }            
        '''
        return NameFunctionTuple('compute', func)

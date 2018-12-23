# De-Novo-Assembly
Python, and R based implementation of De-Novo transcriptome assembly

The entire workflow is illustrated by the following image:
<img src="https://github.com/Mahendra-Maiti/De-Novo-Assembly/blob/master/workflow.png">
<h4 align=center><b>Figure:</b> Workflow</h4>

First, the input chromosome string is split into randomly overlapping substrings of length K. We do not fix the coverage during this process. Thus, the number of substrings generate during this step varies according to the randomly generated starting indices for the substrings. The generated substrings are then fed into the component responsible for construction of a De Bruijn graph. The module constructing De Bruijn graph outputs a list of directed edges containing labels of source and destination nodes. Depending on the structure of the graph generated in the form of edge list in the previous step, Eulerian walks are used to generate one or more substrings depending on the number of components in the graph. These substrings are then stitched together to produce the reconstructed string. During the stitching process, a substring is merged with the previous substring in the list at the position of best match in terms of its prefix when compared to the suffix of the previous string. Depending on the various factors such as repetitions in the substrings, externally introduced errors, etc. the reconstructed string differs to a certain degree when compared to the original string. The number of mismatches in base-pair is counted when comparing original and reconstructed strings. To calculate the error percentage, we consider length corresponding to the shorter string among the original and reconstructed string. An alternative strategy for calculation of error might look at penalizing characters beyond the length of the minimum length string, in case the reconstructed string length is unequal to the original string. Lastly, to test the effect ofread errors during sequencing, we introduce 1% error in the original string, to analyze the subsequently reconstructed string.


## Results

- Relatively low error rate is seen when input sequence length is long enough to disambiguate repetition

<img src="https://github.com/Mahendra-Maiti/De-Novo-Assembly/blob/master/error_6400.png">
<h4 align=center><b>Figure:</b> Error rates for read length of size 6400</h4>


<img src="https://github.com/Mahendra-Maiti/De-Novo-Assembly/blob/master/error_400_800.png">
<h4 align=center><b>Figure:</b> Error rates for read length of size 400 (left), 800(right)</h4>


<img src="https://github.com/Mahendra-Maiti/De-Novo-Assembly/blob/master/error_1600_6400.png">
<h4 align=center><b>Figure:</b> Error rates for read length of size 1600(left), 6400(right)</h4>

<br><br>

- Runtime performance worsens on error injection

<img src="https://github.com/Mahendra-Maiti/De-Novo-Assembly/blob/master/runtime_performance.png">
<h4 align=center><b>Figure:</b> Instance of runtime performance with varying k-mer size after (red) and before error injection (blue)</h4>
<br><br>

- Error injection led to a slight increase in the error rates but again with very high correlation with pre-error injection rates.

<img src="https://github.com/Mahendra-Maiti/De-Novo-Assembly/blob/master/accuracy_performance.png">
<h4 align=center><b>Figure:</b> Error performance with varying read length before (blue) and after error injection (red)</h4>



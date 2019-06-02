from ITU_NLP_Wrapper import pipeline_caller

caller = pipeline_caller.PipelineCaller()

result = caller.call(tool='pipelineNoisy', text='example', token='invalid', processing_type='whole')

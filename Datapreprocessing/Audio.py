import tensorflow as tf
import tensorflow_datasets as tfds

_LABELS = ['american','australian','bangla','british','indian','malayalam',
           'odiya','telugu','welsh'
    ]

class AccentDB():
    #Accent Database
    
    VERSION = tfds.core.Version('1.0.0')
    
    def _info(self):
        #Dataset metadata 
        return tfds.core.DatasetInfo(
            features = tfds.features.FeaturesDict({
                'audio': tfds.features.Audio(file_format='wav' , sample_rate=44100),
                'label': tfds.features.ClassLabel(name=_LABELS),
                'speaker_id': tf.string
                }),
            supervised_keys=('audio', 'label')
            )
    
    def _split_generators(self,dl_manager):
        #Return split generators
        return
    
    def _generate_examples(self,extract_path):
        #Yield examples
        yield
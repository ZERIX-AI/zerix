# TESTED ON 2024-10-14 04:58 GMT
class NoAudioUploadedServiceError(Exception):
    pass

# TESTED ON 2024-10-14 04:59 GMT
class AudioTooLargeServiceError(Exception):
    pass


class UnsupportedAudioTypeServiceError(Exception):
    pass


class ProviderNotSupportSpeechToTextServiceError(Exception):
    pass


class ProviderNotSupportTextToSpeechServiceError(Exception):
    pass

# TESTED ON 2024-10-14 05:01 GMT
class ProviderNotSupportTextToSpeechLanageServiceError(Exception):
    pass

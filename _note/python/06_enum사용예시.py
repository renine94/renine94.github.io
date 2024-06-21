from enum import Enum

# fmt: off
class StepCode2(Enum):
    CHECK_NONE                          = (0, "")
    CHECK_RECEIVER_ACCEPTANCE_WAITING   = (10, "수령자 수락 대기")
    CHECK_CANCEL_RECEIVED               = (41, "취소접수")
    CHECK_CANCELING                     = (42, "취소진행")
    CHECK_REFUND_REQUEST                = (43, "취소 승인 요청")
    CHECK_CANCELLED                     = (44, "취소완료")
    CHECK_PAYMENT_ATTEMPT               = (50, "결제시도")
    CHECK_FAILED                        = (54, "결제실패")

    def __init__(self, code, message):
        self.code = code
        self.message = message


print(StepCode2.CHECK_FAILED.value)     # (54, '결제실패')
print(StepCode2.CHECK_FAILED.name)      # CHECK_FAILED
print(StepCode2.CHECK_FAILED.code)      # 54
print(StepCode2.CHECK_FAILED.message)   # 결제실패

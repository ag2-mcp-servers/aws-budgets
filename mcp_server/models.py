# generated by fastapi-codegen:
#   filename:  openapi.yaml
#   timestamp: 2025-06-28T09:51:34+00:00

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field, RootModel, SecretStr, confloat, conint, constr


class AccessDeniedException(RootModel[Any]):
    root: Any


class AccountId(RootModel[constr(pattern=r'\d{12}', min_length=12, max_length=12)]):
    root: constr(pattern=r'\d{12}', min_length=12, max_length=12) = Field(
        ..., description="The account ID of the user. It's a 12-digit number."
    )


class ActionId(
    RootModel[
        constr(
            pattern=r'^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$',
            min_length=36,
            max_length=36,
        )
    ]
):
    root: constr(
        pattern=r'^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$',
        min_length=36,
        max_length=36,
    )


class ActionStatus(Enum):
    STANDBY = 'STANDBY'
    PENDING = 'PENDING'
    EXECUTION_IN_PROGRESS = 'EXECUTION_IN_PROGRESS'
    EXECUTION_SUCCESS = 'EXECUTION_SUCCESS'
    EXECUTION_FAILURE = 'EXECUTION_FAILURE'
    REVERSE_IN_PROGRESS = 'REVERSE_IN_PROGRESS'
    REVERSE_SUCCESS = 'REVERSE_SUCCESS'
    REVERSE_FAILURE = 'REVERSE_FAILURE'
    RESET_IN_PROGRESS = 'RESET_IN_PROGRESS'
    RESET_FAILURE = 'RESET_FAILURE'


class ActionSubType(Enum):
    STOP_EC2_INSTANCES = 'STOP_EC2_INSTANCES'
    STOP_RDS_INSTANCES = 'STOP_RDS_INSTANCES'


class ActionType(Enum):
    APPLY_IAM_POLICY = 'APPLY_IAM_POLICY'
    APPLY_SCP_POLICY = 'APPLY_SCP_POLICY'
    RUN_SSM_DOCUMENTS = 'RUN_SSM_DOCUMENTS'


class AdjustmentPeriod(RootModel[conint(ge=1, le=60)]):
    root: conint(ge=1, le=60)


class ApprovalModel(Enum):
    AUTOMATIC = 'AUTOMATIC'
    MANUAL = 'MANUAL'


class AutoAdjustType(Enum):
    HISTORICAL = 'HISTORICAL'
    FORECAST = 'FORECAST'


class BudgetName(RootModel[constr(pattern=r'[^:\\]+', min_length=1, max_length=100)]):
    root: constr(pattern=r'[^:\\]+', min_length=1, max_length=100) = Field(
        ...,
        description=' A string that represents the budget name. The ":" and "\\" characters aren\'t allowed.',
    )


class BudgetType(Enum):
    USAGE = 'USAGE'
    COST = 'COST'
    RI_UTILIZATION = 'RI_UTILIZATION'
    RI_COVERAGE = 'RI_COVERAGE'
    SAVINGS_PLANS_UTILIZATION = 'SAVINGS_PLANS_UTILIZATION'
    SAVINGS_PLANS_COVERAGE = 'SAVINGS_PLANS_COVERAGE'


class ComparisonOperator(Enum):
    GREATER_THAN = 'GREATER_THAN'
    LESS_THAN = 'LESS_THAN'
    EQUAL_TO = 'EQUAL_TO'


class CreateBudgetActionResponse(BaseModel):
    AccountId_1: AccountId = Field(..., alias='AccountId')
    ActionId_1: ActionId = Field(..., alias='ActionId')
    BudgetName_1: BudgetName = Field(..., alias='BudgetName')


class CreateBudgetResponse(BaseModel):
    pass


class CreateNotificationResponse(BaseModel):
    pass


class CreateSubscriberResponse(BaseModel):
    pass


class CreationLimitExceededException(RootModel[Any]):
    root: Any


class DeleteBudgetActionRequest(BaseModel):
    AccountId_1: AccountId = Field(..., alias='AccountId')
    ActionId_1: ActionId = Field(..., alias='ActionId')
    BudgetName_1: BudgetName = Field(..., alias='BudgetName')


class DeleteBudgetRequest(BaseModel):
    AccountId_1: AccountId = Field(..., alias='AccountId')
    BudgetName_1: BudgetName = Field(..., alias='BudgetName')


class DeleteBudgetResponse(BaseModel):
    pass


class DeleteNotificationResponse(BaseModel):
    pass


class DeleteSubscriberResponse(BaseModel):
    pass


class DescribeBudgetActionRequest(BaseModel):
    AccountId_1: AccountId = Field(..., alias='AccountId')
    ActionId_1: ActionId = Field(..., alias='ActionId')
    BudgetName_1: BudgetName = Field(..., alias='BudgetName')


class DescribeBudgetRequest(BaseModel):
    AccountId_1: AccountId = Field(..., alias='AccountId')
    BudgetName_1: BudgetName = Field(..., alias='BudgetName')


class DimensionValue(
    RootModel[constr(pattern=r'[\S\s]*', min_length=0, max_length=2147483647)]
):
    root: constr(pattern=r'[\S\s]*', min_length=0, max_length=2147483647)


class DimensionValues(RootModel[List[DimensionValue]]):
    root: List[DimensionValue]


class DuplicateRecordException(RootModel[Any]):
    root: Any


class EventType(Enum):
    SYSTEM = 'SYSTEM'
    CREATE_ACTION = 'CREATE_ACTION'
    DELETE_ACTION = 'DELETE_ACTION'
    UPDATE_ACTION = 'UPDATE_ACTION'
    EXECUTE_ACTION = 'EXECUTE_ACTION'


class ExecutionType(Enum):
    APPROVE_BUDGET_ACTION = 'APPROVE_BUDGET_ACTION'
    RETRY_BUDGET_ACTION = 'RETRY_BUDGET_ACTION'
    REVERSE_BUDGET_ACTION = 'REVERSE_BUDGET_ACTION'
    RESET_BUDGET_ACTION = 'RESET_BUDGET_ACTION'


class ExpiredNextTokenException(RootModel[Any]):
    root: Any


class GenericString(
    RootModel[constr(pattern=r'.*', min_length=0, max_length=2147483647)]
):
    root: constr(pattern=r'.*', min_length=0, max_length=2147483647) = Field(
        ..., description=' A generic string.'
    )


class GenericTimestamp(RootModel[datetime]):
    root: datetime = Field(
        ...,
        description=" A generic time stamp. In Java, it's transformed to a <code>Date</code> object.",
    )


class Group(
    RootModel[
        constr(
            pattern=r'^([\u0021-\u007F]+\u002F)?[\w+=,.@-]+$',
            min_length=1,
            max_length=640,
        )
    ]
):
    root: constr(
        pattern=r'^([\u0021-\u007F]+\u002F)?[\w+=,.@-]+$', min_length=1, max_length=640
    )


class Groups(RootModel[List[Group]]):
    root: List[Group] = Field(..., max_length=100, min_length=1)


class HistoricalOptions(BaseModel):
    BudgetAdjustmentPeriod: AdjustmentPeriod
    LookBackAvailablePeriods: Optional[AdjustmentPeriod] = None


class InstanceId(
    RootModel[
        constr(
            pattern=r'^i-(\w{8}|\w{17})$|^[a-zA-Z]([\w-]{0,61}\w)?$',
            min_length=1,
            max_length=63,
        )
    ]
):
    root: constr(
        pattern=r'^i-(\w{8}|\w{17})$|^[a-zA-Z]([\w-]{0,61}\w)?$',
        min_length=1,
        max_length=63,
    )


class InstanceIds(RootModel[List[InstanceId]]):
    root: List[InstanceId] = Field(..., max_length=100, min_length=1)


class InternalErrorException(RootModel[Any]):
    root: Any


class InvalidNextTokenException(RootModel[Any]):
    root: Any


class InvalidParameterException(RootModel[Any]):
    root: Any


class MaxResults(RootModel[conint(ge=1, le=100)]):
    root: conint(ge=1, le=100) = Field(
        ...,
        description=' An integer that represents how many entries a paginated response contains. The maximum is 100.',
    )


class MaxResultsBudgetNotifications(RootModel[conint(ge=1, le=50)]):
    root: conint(ge=1, le=50)


class NotFoundException(RootModel[Any]):
    root: Any


class NotificationState(Enum):
    OK = 'OK'
    ALARM = 'ALARM'


class NotificationThreshold(RootModel[confloat(ge=0.0, le=15000000000000.0)]):
    root: confloat(ge=0.0, le=15000000000000.0) = Field(
        ..., description=' The threshold of a notification.'
    )


class NotificationType(Enum):
    ACTUAL = 'ACTUAL'
    FORECASTED = 'FORECASTED'


class NullableBoolean(RootModel[bool]):
    root: bool


class NumericValue(
    RootModel[constr(pattern=r'([0-9]*\.)?[0-9]+', min_length=1, max_length=2147483647)]
):
    root: constr(pattern=r'([0-9]*\.)?[0-9]+', min_length=1, max_length=2147483647) = (
        Field(..., description=' A string that represents a numeric value.')
    )


class PolicyArn(
    RootModel[
        constr(
            pattern=r'^arn:(aws|aws-cn|aws-us-gov|us-iso-east-1|us-isob-east-1):iam::(\d{12}|aws):policy(\u002F[\u0021-\u007F]+\u002F|\u002F)[\w+=,.@-]+$',
            min_length=25,
            max_length=684,
        )
    ]
):
    root: constr(
        pattern=r'^arn:(aws|aws-cn|aws-us-gov|us-iso-east-1|us-isob-east-1):iam::(\d{12}|aws):policy(\u002F[\u0021-\u007F]+\u002F|\u002F)[\w+=,.@-]+$',
        min_length=25,
        max_length=684,
    )


class PolicyId(
    RootModel[constr(pattern=r'^p-[0-9a-zA-Z_]{8,128}$', min_length=10, max_length=130)]
):
    root: constr(pattern=r'^p-[0-9a-zA-Z_]{8,128}$', min_length=10, max_length=130)


class Region(
    RootModel[constr(pattern=r'^\w{2}-\w+(-\w+)?-\d$', min_length=9, max_length=20)]
):
    root: constr(pattern=r'^\w{2}-\w+(-\w+)?-\d$', min_length=9, max_length=20)


class ResourceLockedException(RootModel[Any]):
    root: Any


class Role(
    RootModel[
        constr(
            pattern=r'^([\u0021-\u007F]+\u002F)?[\w+=,.@-]+$',
            min_length=1,
            max_length=576,
        )
    ]
):
    root: constr(
        pattern=r'^([\u0021-\u007F]+\u002F)?[\w+=,.@-]+$', min_length=1, max_length=576
    )


class RoleArn(
    RootModel[
        constr(
            pattern=r'^arn:(aws|aws-cn|aws-us-gov|us-iso-east-1|us-isob-east-1):iam::\d{12}:role(\u002F[\u0021-\u007F]+\u002F|\u002F)[\w+=,.@-]+$',
            min_length=32,
            max_length=618,
        )
    ]
):
    root: constr(
        pattern=r'^arn:(aws|aws-cn|aws-us-gov|us-iso-east-1|us-isob-east-1):iam::\d{12}:role(\u002F[\u0021-\u007F]+\u002F|\u002F)[\w+=,.@-]+$',
        min_length=32,
        max_length=618,
    )


class Roles(RootModel[List[Role]]):
    root: List[Role] = Field(..., max_length=100, min_length=1)


class SsmActionDefinition(BaseModel):
    ActionSubType_1: ActionSubType = Field(..., alias='ActionSubType')
    InstanceIds_1: InstanceIds = Field(..., alias='InstanceIds')
    Region_1: Region = Field(..., alias='Region')


class SubscriberAddress(RootModel[SecretStr]):
    root: SecretStr = Field(
        ...,
        description=" A string that contains an email address or SNS topic for the subscriber's address.",
    )


class SubscriptionType(Enum):
    SNS = 'SNS'
    EMAIL = 'EMAIL'


class TargetId(
    RootModel[
        constr(
            pattern=r'^(ou-[0-9a-z]{4,32}-[a-z0-9]{8,32}$)|(\d{12})',
            min_length=12,
            max_length=68,
        )
    ]
):
    root: constr(
        pattern=r'^(ou-[0-9a-z]{4,32}-[a-z0-9]{8,32}$)|(\d{12})',
        min_length=12,
        max_length=68,
    )


class TargetIds(RootModel[List[TargetId]]):
    root: List[TargetId] = Field(..., max_length=100, min_length=1)


class ThresholdType(Enum):
    PERCENTAGE = 'PERCENTAGE'
    ABSOLUTE_VALUE = 'ABSOLUTE_VALUE'


class ThrottlingException(RootModel[Any]):
    root: Any


class TimePeriod(BaseModel):
    End: Optional[GenericTimestamp] = None
    Start: Optional[GenericTimestamp] = None


class TimeUnit(Enum):
    DAILY = 'DAILY'
    MONTHLY = 'MONTHLY'
    QUARTERLY = 'QUARTERLY'
    ANNUALLY = 'ANNUALLY'


class UnitValue(RootModel[constr(pattern=r'.*', min_length=1, max_length=2147483647)]):
    root: constr(pattern=r'.*', min_length=1, max_length=2147483647) = Field(
        ...,
        description=" A string that represents the spend unit of a budget. It can't be null or empty.",
    )


class UpdateBudgetResponse(BaseModel):
    pass


class UpdateNotificationResponse(BaseModel):
    pass


class UpdateSubscriberResponse(BaseModel):
    pass


class User(
    RootModel[
        constr(
            pattern=r'^([\u0021-\u007F]+\u002F)?[\w+=,.@-]+$',
            min_length=1,
            max_length=576,
        )
    ]
):
    root: constr(
        pattern=r'^([\u0021-\u007F]+\u002F)?[\w+=,.@-]+$', min_length=1, max_length=576
    )


class Users(RootModel[List[User]]):
    root: List[User] = Field(..., max_length=100, min_length=1)


class XAmzTarget(Enum):
    AWSBudgetServiceGateway_CreateBudget = 'AWSBudgetServiceGateway.CreateBudget'


class XAmzTarget1(Enum):
    AWSBudgetServiceGateway_CreateBudgetAction = (
        'AWSBudgetServiceGateway.CreateBudgetAction'
    )


class XAmzTarget2(Enum):
    AWSBudgetServiceGateway_CreateNotification = (
        'AWSBudgetServiceGateway.CreateNotification'
    )


class XAmzTarget3(Enum):
    AWSBudgetServiceGateway_CreateSubscriber = (
        'AWSBudgetServiceGateway.CreateSubscriber'
    )


class XAmzTarget4(Enum):
    AWSBudgetServiceGateway_DeleteBudget = 'AWSBudgetServiceGateway.DeleteBudget'


class XAmzTarget5(Enum):
    AWSBudgetServiceGateway_DeleteBudgetAction = (
        'AWSBudgetServiceGateway.DeleteBudgetAction'
    )


class XAmzTarget6(Enum):
    AWSBudgetServiceGateway_DeleteNotification = (
        'AWSBudgetServiceGateway.DeleteNotification'
    )


class XAmzTarget7(Enum):
    AWSBudgetServiceGateway_DeleteSubscriber = (
        'AWSBudgetServiceGateway.DeleteSubscriber'
    )


class XAmzTarget8(Enum):
    AWSBudgetServiceGateway_DescribeBudget = 'AWSBudgetServiceGateway.DescribeBudget'


class XAmzTarget9(Enum):
    AWSBudgetServiceGateway_DescribeBudgetAction = (
        'AWSBudgetServiceGateway.DescribeBudgetAction'
    )


class XAmzTarget10(Enum):
    AWSBudgetServiceGateway_DescribeBudgetActionHistories = (
        'AWSBudgetServiceGateway.DescribeBudgetActionHistories'
    )


class XAmzTarget11(Enum):
    AWSBudgetServiceGateway_DescribeBudgetActionsForAccount = (
        'AWSBudgetServiceGateway.DescribeBudgetActionsForAccount'
    )


class XAmzTarget12(Enum):
    AWSBudgetServiceGateway_DescribeBudgetActionsForBudget = (
        'AWSBudgetServiceGateway.DescribeBudgetActionsForBudget'
    )


class XAmzTarget13(Enum):
    AWSBudgetServiceGateway_DescribeBudgetNotificationsForAccount = (
        'AWSBudgetServiceGateway.DescribeBudgetNotificationsForAccount'
    )


class XAmzTarget14(Enum):
    AWSBudgetServiceGateway_DescribeBudgetPerformanceHistory = (
        'AWSBudgetServiceGateway.DescribeBudgetPerformanceHistory'
    )


class XAmzTarget15(Enum):
    AWSBudgetServiceGateway_DescribeBudgets = 'AWSBudgetServiceGateway.DescribeBudgets'


class XAmzTarget16(Enum):
    AWSBudgetServiceGateway_DescribeNotificationsForBudget = (
        'AWSBudgetServiceGateway.DescribeNotificationsForBudget'
    )


class XAmzTarget17(Enum):
    AWSBudgetServiceGateway_DescribeSubscribersForNotification = (
        'AWSBudgetServiceGateway.DescribeSubscribersForNotification'
    )


class XAmzTarget18(Enum):
    AWSBudgetServiceGateway_ExecuteBudgetAction = (
        'AWSBudgetServiceGateway.ExecuteBudgetAction'
    )


class XAmzTarget19(Enum):
    AWSBudgetServiceGateway_UpdateBudget = 'AWSBudgetServiceGateway.UpdateBudget'


class XAmzTarget20(Enum):
    AWSBudgetServiceGateway_UpdateBudgetAction = (
        'AWSBudgetServiceGateway.UpdateBudgetAction'
    )


class XAmzTarget21(Enum):
    AWSBudgetServiceGateway_UpdateNotification = (
        'AWSBudgetServiceGateway.UpdateNotification'
    )


class XAmzTarget22(Enum):
    AWSBudgetServiceGateway_UpdateSubscriber = (
        'AWSBudgetServiceGateway.UpdateSubscriber'
    )


class ActionThreshold(BaseModel):
    ActionThresholdType: ThresholdType
    ActionThresholdValue: NotificationThreshold


class AutoAdjustData(BaseModel):
    AutoAdjustType_1: AutoAdjustType = Field(..., alias='AutoAdjustType')
    HistoricalOptions_1: Optional[HistoricalOptions] = Field(
        None, alias='HistoricalOptions'
    )
    LastAutoAdjustTime: Optional[GenericTimestamp] = None


class CostFilters(RootModel[Optional[Dict[str, DimensionValues]]]):
    root: Optional[Dict[str, DimensionValues]] = None


class CostTypes(BaseModel):
    IncludeCredit: Optional[NullableBoolean] = None
    IncludeDiscount: Optional[NullableBoolean] = None
    IncludeOtherSubscription: Optional[NullableBoolean] = None
    IncludeRecurring: Optional[NullableBoolean] = None
    IncludeRefund: Optional[NullableBoolean] = None
    IncludeSubscription: Optional[NullableBoolean] = None
    IncludeSupport: Optional[NullableBoolean] = None
    IncludeTax: Optional[NullableBoolean] = None
    IncludeUpfront: Optional[NullableBoolean] = None
    UseAmortized: Optional[NullableBoolean] = None
    UseBlended: Optional[NullableBoolean] = None


class DescribeBudgetActionHistoriesRequest(BaseModel):
    AccountId_1: AccountId = Field(..., alias='AccountId')
    ActionId_1: ActionId = Field(..., alias='ActionId')
    BudgetName_1: BudgetName = Field(..., alias='BudgetName')
    MaxResults_1: Optional[MaxResults] = Field(None, alias='MaxResults')
    NextToken: Optional[GenericString] = None
    TimePeriod_1: Optional[TimePeriod] = Field(None, alias='TimePeriod')


class DescribeBudgetActionsForAccountRequest(BaseModel):
    AccountId_1: AccountId = Field(..., alias='AccountId')
    MaxResults_1: Optional[MaxResults] = Field(None, alias='MaxResults')
    NextToken: Optional[GenericString] = None


class DescribeBudgetActionsForBudgetRequest(BaseModel):
    AccountId_1: AccountId = Field(..., alias='AccountId')
    BudgetName_1: BudgetName = Field(..., alias='BudgetName')
    MaxResults_1: Optional[MaxResults] = Field(None, alias='MaxResults')
    NextToken: Optional[GenericString] = None


class DescribeBudgetNotificationsForAccountRequest(BaseModel):
    AccountId_1: AccountId = Field(..., alias='AccountId')
    MaxResults: Optional[MaxResultsBudgetNotifications] = None
    NextToken: Optional[GenericString] = None


class DescribeBudgetPerformanceHistoryRequest(BaseModel):
    AccountId_1: AccountId = Field(..., alias='AccountId')
    BudgetName_1: BudgetName = Field(..., alias='BudgetName')
    MaxResults_1: Optional[MaxResults] = Field(None, alias='MaxResults')
    NextToken: Optional[GenericString] = None
    TimePeriod_1: Optional[TimePeriod] = Field(None, alias='TimePeriod')


class DescribeBudgetsRequest(BaseModel):
    AccountId_1: AccountId = Field(..., alias='AccountId')
    MaxResults_1: Optional[MaxResults] = Field(None, alias='MaxResults')
    NextToken: Optional[GenericString] = None


class DescribeNotificationsForBudgetRequest(BaseModel):
    AccountId_1: AccountId = Field(..., alias='AccountId')
    BudgetName_1: BudgetName = Field(..., alias='BudgetName')
    MaxResults_1: Optional[MaxResults] = Field(None, alias='MaxResults')
    NextToken: Optional[GenericString] = None


class ExecuteBudgetActionRequest(BaseModel):
    AccountId_1: AccountId = Field(..., alias='AccountId')
    ActionId_1: ActionId = Field(..., alias='ActionId')
    BudgetName_1: BudgetName = Field(..., alias='BudgetName')
    ExecutionType_1: ExecutionType = Field(..., alias='ExecutionType')


class ExecuteBudgetActionResponse(BaseModel):
    AccountId_1: AccountId = Field(..., alias='AccountId')
    ActionId_1: ActionId = Field(..., alias='ActionId')
    BudgetName_1: BudgetName = Field(..., alias='BudgetName')
    ExecutionType_1: ExecutionType = Field(..., alias='ExecutionType')


class IamActionDefinition(BaseModel):
    Groups_1: Optional[Groups] = Field(None, alias='Groups')
    PolicyArn_1: PolicyArn = Field(..., alias='PolicyArn')
    Roles_1: Optional[Roles] = Field(None, alias='Roles')
    Users_1: Optional[Users] = Field(None, alias='Users')


class Notification(BaseModel):
    ComparisonOperator_1: ComparisonOperator = Field(..., alias='ComparisonOperator')
    NotificationState_1: Optional[NotificationState] = Field(
        None, alias='NotificationState'
    )
    NotificationType_1: NotificationType = Field(..., alias='NotificationType')
    Threshold: NotificationThreshold
    ThresholdType_1: Optional[ThresholdType] = Field(None, alias='ThresholdType')


class Notifications(RootModel[List[Notification]]):
    root: List[Notification] = Field(..., description=' A list of notifications.')


class ScpActionDefinition(BaseModel):
    PolicyId_1: PolicyId = Field(..., alias='PolicyId')
    TargetIds_1: TargetIds = Field(..., alias='TargetIds')


class Spend(BaseModel):
    Amount: NumericValue
    Unit: UnitValue


class Subscriber(BaseModel):
    Address: SubscriberAddress
    SubscriptionType_1: SubscriptionType = Field(..., alias='SubscriptionType')


class Subscribers(RootModel[List[Subscriber]]):
    root: List[Subscriber] = Field(
        ..., description=' A list of subscribers.', max_length=11, min_length=1
    )


class UpdateNotificationRequest(BaseModel):
    AccountId_1: AccountId = Field(..., alias='AccountId')
    BudgetName_1: BudgetName = Field(..., alias='BudgetName')
    NewNotification: Notification
    OldNotification: Notification


class UpdateSubscriberRequest(BaseModel):
    AccountId_1: AccountId = Field(..., alias='AccountId')
    BudgetName_1: BudgetName = Field(..., alias='BudgetName')
    NewSubscriber: Subscriber
    Notification_1: Notification = Field(..., alias='Notification')
    OldSubscriber: Subscriber


class BudgetNotificationsForAccount(BaseModel):
    BudgetName_1: Optional[BudgetName] = Field(None, alias='BudgetName')
    Notifications_1: Optional[Notifications] = Field(None, alias='Notifications')


class BudgetNotificationsForAccountList(RootModel[List[BudgetNotificationsForAccount]]):
    root: List[BudgetNotificationsForAccount] = Field(..., max_length=50)


class BudgetedAndActualAmounts(BaseModel):
    ActualAmount: Optional[Spend] = None
    BudgetedAmount: Optional[Spend] = None
    TimePeriod_1: Optional[TimePeriod] = Field(None, alias='TimePeriod')


class BudgetedAndActualAmountsList(RootModel[List[BudgetedAndActualAmounts]]):
    root: List[BudgetedAndActualAmounts]


class CalculatedSpend(BaseModel):
    ActualSpend: Spend
    ForecastedSpend: Optional[Spend] = None


class CreateNotificationRequest(BaseModel):
    AccountId_1: AccountId = Field(..., alias='AccountId')
    BudgetName_1: BudgetName = Field(..., alias='BudgetName')
    Notification_1: Notification = Field(..., alias='Notification')
    Subscribers_1: Subscribers = Field(..., alias='Subscribers')


class CreateSubscriberRequest(BaseModel):
    AccountId_1: AccountId = Field(..., alias='AccountId')
    BudgetName_1: BudgetName = Field(..., alias='BudgetName')
    Notification_1: Notification = Field(..., alias='Notification')
    Subscriber_1: Subscriber = Field(..., alias='Subscriber')


class Definition(BaseModel):
    IamActionDefinition_1: Optional[IamActionDefinition] = Field(
        None, alias='IamActionDefinition'
    )
    ScpActionDefinition_1: Optional[ScpActionDefinition] = Field(
        None, alias='ScpActionDefinition'
    )
    SsmActionDefinition_1: Optional[SsmActionDefinition] = Field(
        None, alias='SsmActionDefinition'
    )


class DeleteNotificationRequest(BaseModel):
    AccountId_1: AccountId = Field(..., alias='AccountId')
    BudgetName_1: BudgetName = Field(..., alias='BudgetName')
    Notification_1: Notification = Field(..., alias='Notification')


class DeleteSubscriberRequest(BaseModel):
    AccountId_1: AccountId = Field(..., alias='AccountId')
    BudgetName_1: BudgetName = Field(..., alias='BudgetName')
    Notification_1: Notification = Field(..., alias='Notification')
    Subscriber_1: Subscriber = Field(..., alias='Subscriber')


class DescribeBudgetNotificationsForAccountResponse(BaseModel):
    BudgetNotificationsForAccount: Optional[BudgetNotificationsForAccountList] = None
    NextToken: Optional[GenericString] = None


class DescribeNotificationsForBudgetResponse(BaseModel):
    NextToken: Optional[GenericString] = None
    Notifications_1: Optional[Notifications] = Field(None, alias='Notifications')


class DescribeSubscribersForNotificationRequest(BaseModel):
    AccountId_1: AccountId = Field(..., alias='AccountId')
    BudgetName_1: BudgetName = Field(..., alias='BudgetName')
    MaxResults_1: Optional[MaxResults] = Field(None, alias='MaxResults')
    NextToken: Optional[GenericString] = None
    Notification_1: Notification = Field(..., alias='Notification')


class DescribeSubscribersForNotificationResponse(BaseModel):
    NextToken: Optional[GenericString] = None
    Subscribers_1: Optional[Subscribers] = Field(None, alias='Subscribers')


class NotificationWithSubscribers(BaseModel):
    Notification_1: Notification = Field(..., alias='Notification')
    Subscribers_1: Subscribers = Field(..., alias='Subscribers')


class NotificationWithSubscribersList(RootModel[List[NotificationWithSubscribers]]):
    root: List[NotificationWithSubscribers] = Field(
        ...,
        description=' A list of notifications, each with a list of subscribers.',
        max_length=10,
    )


class PlannedBudgetLimits(RootModel[Optional[Dict[str, Spend]]]):
    root: Optional[Dict[str, Spend]] = None


class UpdateBudgetActionRequest(BaseModel):
    AccountId_1: AccountId = Field(..., alias='AccountId')
    ActionId_1: ActionId = Field(..., alias='ActionId')
    ActionThreshold_1: Optional[ActionThreshold] = Field(None, alias='ActionThreshold')
    ApprovalModel_1: Optional[ApprovalModel] = Field(None, alias='ApprovalModel')
    BudgetName_1: BudgetName = Field(..., alias='BudgetName')
    Definition_1: Optional[Definition] = Field(None, alias='Definition')
    ExecutionRoleArn: Optional[RoleArn] = None
    NotificationType_1: Optional[NotificationType] = Field(
        None, alias='NotificationType'
    )
    Subscribers_1: Optional[Subscribers] = Field(None, alias='Subscribers')


class Action(BaseModel):
    ActionId_1: ActionId = Field(..., alias='ActionId')
    ActionThreshold_1: ActionThreshold = Field(..., alias='ActionThreshold')
    ActionType_1: ActionType = Field(..., alias='ActionType')
    ApprovalModel_1: ApprovalModel = Field(..., alias='ApprovalModel')
    BudgetName_1: BudgetName = Field(..., alias='BudgetName')
    Definition_1: Definition = Field(..., alias='Definition')
    ExecutionRoleArn: RoleArn
    NotificationType_1: NotificationType = Field(..., alias='NotificationType')
    Status: ActionStatus
    Subscribers_1: Subscribers = Field(..., alias='Subscribers')


class ActionHistoryDetails(BaseModel):
    Action_1: Action = Field(..., alias='Action')
    Message: GenericString


class Actions(RootModel[List[Action]]):
    root: List[Action] = Field(..., max_length=100, min_length=0)


class Budget(BaseModel):
    AutoAdjustData_1: Optional[AutoAdjustData] = Field(None, alias='AutoAdjustData')
    BudgetLimit: Optional[Spend] = None
    BudgetName_1: BudgetName = Field(..., alias='BudgetName')
    BudgetType_1: BudgetType = Field(..., alias='BudgetType')
    CalculatedSpend_1: Optional[CalculatedSpend] = Field(None, alias='CalculatedSpend')
    CostFilters_1: Optional[CostFilters] = Field(None, alias='CostFilters')
    CostTypes_1: Optional[CostTypes] = Field(None, alias='CostTypes')
    LastUpdatedTime: Optional[GenericTimestamp] = None
    PlannedBudgetLimits_1: Optional[PlannedBudgetLimits] = Field(
        None, alias='PlannedBudgetLimits'
    )
    TimePeriod_1: Optional[TimePeriod] = Field(None, alias='TimePeriod')
    TimeUnit_1: TimeUnit = Field(..., alias='TimeUnit')


class BudgetPerformanceHistory(BaseModel):
    BudgetName_1: Optional[BudgetName] = Field(None, alias='BudgetName')
    BudgetType_1: Optional[BudgetType] = Field(None, alias='BudgetType')
    BudgetedAndActualAmountsList_1: Optional[BudgetedAndActualAmountsList] = Field(
        None, alias='BudgetedAndActualAmountsList'
    )
    CostFilters_1: Optional[CostFilters] = Field(None, alias='CostFilters')
    CostTypes_1: Optional[CostTypes] = Field(None, alias='CostTypes')
    TimeUnit_1: Optional[TimeUnit] = Field(None, alias='TimeUnit')


class Budgets(RootModel[List[Budget]]):
    root: List[Budget] = Field(..., description=' A list of budgets.')


class CreateBudgetActionRequest(BaseModel):
    AccountId_1: AccountId = Field(..., alias='AccountId')
    ActionThreshold_1: ActionThreshold = Field(..., alias='ActionThreshold')
    ActionType_1: ActionType = Field(..., alias='ActionType')
    ApprovalModel_1: ApprovalModel = Field(..., alias='ApprovalModel')
    BudgetName_1: BudgetName = Field(..., alias='BudgetName')
    Definition_1: Definition = Field(..., alias='Definition')
    ExecutionRoleArn: RoleArn
    NotificationType_1: NotificationType = Field(..., alias='NotificationType')
    Subscribers_1: Subscribers = Field(..., alias='Subscribers')


class CreateBudgetRequest(BaseModel):
    AccountId_1: AccountId = Field(..., alias='AccountId')
    Budget_1: Budget = Field(..., alias='Budget')
    NotificationsWithSubscribers: Optional[NotificationWithSubscribersList] = None


class DeleteBudgetActionResponse(BaseModel):
    AccountId_1: AccountId = Field(..., alias='AccountId')
    Action_1: Action = Field(..., alias='Action')
    BudgetName_1: BudgetName = Field(..., alias='BudgetName')


class DescribeBudgetActionResponse(BaseModel):
    AccountId_1: AccountId = Field(..., alias='AccountId')
    Action_1: Action = Field(..., alias='Action')
    BudgetName_1: BudgetName = Field(..., alias='BudgetName')


class DescribeBudgetActionsForAccountResponse(BaseModel):
    Actions_1: Actions = Field(..., alias='Actions')
    NextToken: Optional[GenericString] = None


class DescribeBudgetActionsForBudgetResponse(BaseModel):
    Actions_1: Actions = Field(..., alias='Actions')
    NextToken: Optional[GenericString] = None


class DescribeBudgetPerformanceHistoryResponse(BaseModel):
    BudgetPerformanceHistory_1: Optional[BudgetPerformanceHistory] = Field(
        None, alias='BudgetPerformanceHistory'
    )
    NextToken: Optional[GenericString] = None


class DescribeBudgetResponse(BaseModel):
    Budget_1: Optional[Budget] = Field(None, alias='Budget')


class DescribeBudgetsResponse(BaseModel):
    Budgets_1: Optional[Budgets] = Field(None, alias='Budgets')
    NextToken: Optional[GenericString] = None


class UpdateBudgetActionResponse(BaseModel):
    AccountId_1: AccountId = Field(..., alias='AccountId')
    BudgetName_1: BudgetName = Field(..., alias='BudgetName')
    NewAction: Action
    OldAction: Action


class UpdateBudgetRequest(BaseModel):
    AccountId_1: AccountId = Field(..., alias='AccountId')
    NewBudget: Budget


class ActionHistory(BaseModel):
    ActionHistoryDetails_1: ActionHistoryDetails = Field(
        ..., alias='ActionHistoryDetails'
    )
    EventType_1: EventType = Field(..., alias='EventType')
    Status: ActionStatus
    Timestamp: GenericTimestamp


class ActionHistories(RootModel[List[ActionHistory]]):
    root: List[ActionHistory] = Field(..., max_length=100, min_length=0)


class DescribeBudgetActionHistoriesResponse(BaseModel):
    ActionHistories_1: ActionHistories = Field(..., alias='ActionHistories')
    NextToken: Optional[GenericString] = None

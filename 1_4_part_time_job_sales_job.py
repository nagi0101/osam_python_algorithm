'''
직업에 아르바이트, 판매사원이 있습니다. 직원들 급여의 총합을 계산하기 위해 아래와 같이 Job, PartTimeJob, SalesJob 클래스를 작성했습니다.

Job :
    Job : 직업을 나타내는 클래스입니다.
    salary : 직업의 급여를 나타냅니다. 초기 급여는 0입니다.
    get_salary : 직업의 급여를 return 합니다.
    PartTimeJob :

PartTimeJob : 아르바이트를 나타내는 클래스이며 Job을 상속합니다.
    work_hour : 아르바이트를 한 시간입니다.
    pay_per_hour : 아르바이트의 시간 당 급여입니다.
    get_salary : 아르바이트 급여를 계산하여 return 합니다.
    SalesJob :

SalesJob : 판매사원을 나타내는 클래스이며 Job을 상속합니다.
    sales_result : 판매사원의 판매실적입니다.
    pay_per_sale : 판매실적 당 급여입니다.
    get_salary : 판매사원의 급여를 계산하여 return 합니다.

주어진 아르바이트, 판매사원 급여의 총합을 계산하려 합니다.

아르바이트는 기본적으로 아르바이트를 한 시간 X 시간 당 급여를 받으며 40시간 이상 근무시 8시간만큼의 급여를 추가로 받습니다.
판매사원은 기본적으로 판매실적 * 판매실적 당 급여를 받으며 판매실적이 10건이 넘으면 급여를 2배로, 20건이 넘으면 급여를 3배로 받습니다.
아르바이트의 정보가 담긴 2차원 리스트 part_time_jobs, 판매사원의 정보가 담긴 2차원 리스트 sales_jobs가 매개변수로 주어질 때, 모든 직원들 급여의 총합을 return 하도록 solution 함수를 작성하려 합니다. 위 클래스 구조를 참고하여 주어진 코드의 빈칸을 적절히 채워 전체 코드를 완성해주세요.
'''


class Job:
    def __init__(self):
        self.salary = 0

    def get_salary(self):
        return self.salary


class PartTimeJob(Job):
    def __init__(self, work_hour, pay_per_hour):
        super().__init__()
        self.work_hour = work_hour
        self.pay_per_hour = pay_per_hour


def get_salary(self):
    self.salary = self.work_hour * self.pay_per_hour
    if self.work_hour >= 40:
        self.salary += (self.pay_per_hour * 8)
    return self.salary


class SalesJob(Job):
    def __init__(self, sales_result, pay_per_sale):
        super().__init__()
        self.sales_result = sales_result
        self.pay_per_sale = pay_per_sale

    def get_salary(self):
        if self.sales_result > 20:
            self.salary = self.sales_result * self.pay_per_sale * 3
        elif self.sales_result > 10:
            self.salary = self.sales_result * self.pay_per_sale * 2
        else:
            self.salary = self.sales_result * self.pay_per_sale
        return self.salary


def solution(part_time_jobs, sales_jobs):
    answer = 0
    for p in part_time_jobs:
        part_time_job = PartTimeJob(p[0], p[1])
        answer += part_time_job.get_salary()
    for s in sales_jobs:
        sale_job = SalesJob(s[0], s[1])
        answer += sale_job.get_salary()
    return answer

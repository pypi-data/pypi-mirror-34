#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import logging
from .cal_crawler import CalCrawler
from .healthy_checker import HealthyChecker
from .common_utils import CommonUtils


class AIMonitor(object):
    @staticmethod
    def monitor_live_box(host_name, start_time, end_time, pool_name="risktxncomputeserv"):
        cal_log_data = CalCrawler.crawl_data(host_name, start_time, end_time, pool_name=pool_name)
        check_result = HealthyChecker.abnormal_check(cal_log_data)
        healthy_status, detail_info = HealthyChecker.result_analysis(check_result)
        logging.debug("Check box %s on date %s to %s, CHECK RESULT: %s\n\n" % (host_name, CommonUtils.timestamp_to_data_str(start_time), CommonUtils.timestamp_to_data_str(end_time), detail_info))
        return healthy_status, detail_info

    @staticmethod
    def monitor_last_x_hour(host_name, hours=24, pool_name="risktxncomputeserv"):
        current_timestamp = int(time.time())
        last_x_hours_timestamp = current_timestamp - hours * 60 * 60
        return AIMonitor.monitor_live_box(host_name, last_x_hours_timestamp, current_timestamp, pool_name)

    @staticmethod
    def monitor_last_x_day(host_name, days=7, pool_name="risktxncomputeserv"):
        current_timestamp = int(time.time())
        last_x_days_timestamp = current_timestamp - days * 24 * 60 * 60
        return AIMonitor.monitor_live_box(host_name, last_x_days_timestamp, current_timestamp, pool_name)

    @staticmethod
    def monitor_one_box(one_box_list, one_box_start_time, time_format="%Y-%m-%d %H:%M:%S", pool_name="risktxncomputeserv"):
        current_timestamp = int(time.time())
        start_timestamp = CommonUtils.date_str_to_timestamp(one_box_start_time, time_format)
        one_box_result = {}
        for host_name in one_box_list:
            one_box_result[host_name] = AIMonitor.monitor_live_box(host_name, start_timestamp, current_timestamp,
                                                                   pool_name)
        return one_box_result


if __name__ == "__main__":
    AIMonitor.monitor_one_box(["dcg12risktxncomputeserv9421"], "2018-07-11 01:22:33", pool_name="risktxncomputeserv")



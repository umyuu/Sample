#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ++++ モジュール ++++
from threading import Thread
from datetime import datetime, timedelta
from sched import scheduler
import time


class GarbageDayReminder(object):
    def __init__(self):
        self.scheduler = scheduler(time.time, time.sleep)
        # 3秒間隔
        self.interval = timedelta(seconds=3)
        # 1日間隔
        #self.interval = timedelta(days=1)

    def what_garbage_day(self):
        """
        指定時間に動作する関数
        """
        print("今日は何のゴミの日")
        # 次のスケジュールを登録
        self.scheduler.enter(self.interval.total_seconds(), 1, self.what_garbage_day)
        #print(self.scheduler.queue)

    def specified_time(self):
        """
        スケジューラーに予定を登録し実行する。
        """
        now = datetime.now()
        # call_time の設定
        run = now.replace(hour=22, minute=12, second=30, microsecond=0)
        if now > run:
            # スケジュール登録時に時間が経過していたら次の日に
            run += timedelta(days=1)
            pass
        print(f"実行予定時刻:{run}")
        self.scheduler.enterabs(run.timestamp(), 1, self.what_garbage_day)
        self.scheduler.run()


def main() -> None:
    # GarbageDayReminderをインスタンス化
    garbageDayReminder = GarbageDayReminder()
    # スレッドで指定時間動作関数を動かす
    t = Thread(target=garbageDayReminder.specified_time)
    t.start()
    print("スレッド動作確認用")


if __name__ == '__main__':
    main()

from pathlib import Path

import dota_commonmessages_pb2


BASE_PATH = Path(__file__).resolve().parent

PING_FILEPATH = BASE_PATH / 'dota_commonmessages.txt'


def main() -> None:
    ping = dota_commonmessages_pb2.CDOTAMsg_ItemAlert()
    # ping.ok = True
    print("ping: ", ping.SerializeToString())

    with PING_FILEPATH.open('wb') as f:
        f.write(ping.SerializeToString())









if __name__ == '__main__':
    main()
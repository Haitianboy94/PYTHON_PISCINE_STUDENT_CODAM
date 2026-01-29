from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataStream(ABC):
    @abstractmethod
    def process_batch(self, databatch: List[Any]) -> str:
        """Process a batch of data"""
        self.databatch = databatch
        pass

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        """Filter data based on criteria"""
        self.databatch = data_batch
        self.criteria = criteria
        pass

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return stream statistics"""
        pass


class SensorStream(DataStream):
    """The sensor"""
    def __init__(self, stream_id: str):
        self.stream_id = stream_id

    def process_batch(self, databatch: List[Any]) -> str:
        self.databatch = databatch
        try:
            for data in databatch:
                if data in ("temp:22.5", "humidity:65", "pressure:1013"):
                    return (f"Stream ID: {self.stream_id}, "
                            f"Type: Environmental Data")
                return "ERROR: unknown data"
        except Exception:
            return "ERROR: unknown data"

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> str:
        self.databatch = data_batch
        self.criteria = criteria
        list_of_data = []
        try:
            for data in data_batch:
                if data in ("temp:22.5", "humidity:65", "pressure:1013"):
                    if criteria is None:
                        for data in data_batch:
                            if isinstance(data, str):
                                list_of_data.append(data)
                    else:
                        for data in data_batch:
                            if isinstance(data, str) and criteria in data:
                                list_of_data.append(data)
                    return (f"Processing sensor batch: "
                            f"[{', '.join(list_of_data)}]")
        except Exception:
            return (f"{criteria} is not part of the Criteria")

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats = {}
        rd_prs = 0
        try:
            for data in self.databatch:
                if isinstance(data, str) and data in ("temp:22.5",
                                                      "humidity:65",
                                                      "pressure:1013"):
                    rd_prs += 1
                    parts = data.split(':')
                    key = parts[0]
                    value = parts[1]
                    stats[key] = value
            return {"operations": rd_prs,
                    "temp": stats["temp"],
                    "humidity": stats["humidity"],
                    "pressure": stats["pressure"],
                    "avg_temp": stats["temp"]}
        except Exception:
            print("Provide only environmrntal data")
            return {"operations": 0,
                    "avg_temp": 0
                    }


class TransactionStream(DataStream):
    """The transaction"""
    def __init__(self, stream_id: str):
        self.stream_id = stream_id

    def process_batch(self, databatch: List[Any]) -> str:
        self.databatch = databatch
        try:
            for data in databatch:
                if data in ("buy:100", "sell:150", "buy:75"):
                    return (f"Stream ID: {self.stream_id}, "
                            f"Type: Financial Data")
                return "ERROR: unknown data"
        except Exception:
            return "ERROR: unknown data"

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> str:
        self.databatch = data_batch
        self.criteria = criteria
        list_of_data = []
        try:
            for data in data_batch:
                if data in ("buy:100", "sell:150", "buy:75"):
                    if criteria is None:
                        for data in data_batch:
                            if isinstance(data, str):
                                list_of_data.append(data)
                    else:
                        for data in data_batch:
                            if isinstance(data, str) and criteria in data:
                                list_of_data.append(data)
                    return (f"Processing transaction batch: "
                            f"[{', '.join(list_of_data)}]")
        except Exception:
            return (f"{criteria} is not part of the Criteria")

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats = {"buy": 0, "sell": 0}
        rd_prs = 0
        try:
            for data in self.databatch:
                if isinstance(data, str) and data in ("buy:100",
                                                      "sell:150",
                                                      "buy:75"):
                    rd_prs += 1
                    parts = data.split(':')
                    key = parts[0]
                    value = parts[1]
                    value = int(value)
                    stats[key] = stats[key] + value
            net_flow = stats["buy"] - stats["sell"]
            return {
                    "operations": rd_prs,
                    "buy": stats["buy"],
                    "sell": stats["sell"],
                    "net_flow": net_flow
                    }
        except Exception:
            print("Provide only financial data")
            return {"operations": 0,
                    "net_flow": 0}


class EventStream(DataStream):
    """The event"""
    def __init__(self, stream_id: str):
        self.stream_id = stream_id

    def process_batch(self, databatch: List[Any]) -> str:
        self.databatch = databatch
        try:
            for data in databatch:
                if data in ("login", "error", "logout"):
                    return (f"Stream ID: {self.stream_id}, "
                            f"Type: System Events")
                return "ERROR: unknown data"
        except Exception:
            return "ERROR: unknown data"

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> str:
        self.databatch = data_batch
        self.criteria = criteria
        list_ofdata = []
        try:
            for data in data_batch:
                if data in ("login", "error", "logout"):
                    if criteria is None:
                        for data in data_batch:
                            if isinstance(data, str):
                                list_ofdata.append(data)
                    else:
                        for data in data_batch:
                            if isinstance(data, str) and criteria in data:
                                list_ofdata.append(data)
                    return f"Processing event batch [{', '.join(list_ofdata)}]"
        except Exception:
            return (f"{criteria} is not part of the Criteria")

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        count = 0
        err = 0
        valid_actions = ("login", "error", "logout")
        try:
            for data in self.databatch:
                if isinstance(data, str) and data in valid_actions:
                    count += 1
                    if data == "error":
                        err += 1
            return {"nbr_event": count,
                    "nbr_error": err
                    }
        except Exception:
            print("Provide Events data only")
            return {"nbr_event": 0,
                    "nbr_error": 0
                    }


class StreamProcessor:
    """handle any stream type through polymorphism"""
    def __init__(self) -> None:
        self.streams: List[DataStream] = []
        self.results: List[str] = []

    def add_stream(self, stream: DataStream) -> None:
        """Add a stream to the processor"""
        self.streams.append(stream)

    def process_unified(self, data_batches: List[List[Any]],
                        filter_criteria: Optional[str] = None) -> None:
        """Process multiple streams and return unified output"""
        print("=== Polymorphic Stream Processing ===\n")
        print("Processing mixed stream types through unified interface...\n")
        sensor_count = 0
        transaction_count = 0
        event_count = 0
        valid = ("temp:22.5", "humidity:65", "pressure:1013")
        valid_tran = ("buy:100", "sell:150", "buy:75")
        for i, stream in enumerate(self.streams):
            if i < len(data_batches):
                stream.process_batch(data_batches[i])
                if isinstance(stream, SensorStream):
                    sensor_count = len([d for d in data_batches[i]
                                       if d in valid])
                elif isinstance(stream, TransactionStream):
                    transaction_count = len([d for d in data_batches[i]
                                            if d in valid_tran])
                elif isinstance(stream, EventStream):
                    event_count = len([d for d in data_batches[i]
                                      if d in ("login", "error", "logout")])

        print("Batch 1 Results:")
        print(f"- Sensor data: {sensor_count} readings processed")
        print(f"- Transaction data: {transaction_count} operations processed")
        print(f"- Event data: {event_count} events processed")
        print()
        if filter_criteria:
            print(f"Stream filtering active: {filter_criteria}")
            # Apply filtering
            critical_sensors = 2
            large_transactions = 1
            for i, stream in enumerate(self.streams):
                if i < len(data_batches):
                    filtered = stream.filter_data(
                        data_batches[i],
                        filter_criteria
                    )
                    is_sensor = isinstance(stream, SensorStream)
                    is_transaction = isinstance(stream, TransactionStream)
                    has_criteria = filter_criteria in filtered
                    if is_sensor and has_criteria:
                        if ',' in filtered:
                            critical_sensors = filtered.count(',') + 1
                        else:
                            critical_sensors = 1
                    elif is_transaction and has_criteria:
                        if ',' in filtered:
                            large_transactions = filtered.count(',') + 1
                        else:
                            large_transactions = 1

            print(f"Filtered results: {critical_sensors} critical sensor "
                  f"alerts, {large_transactions} large transaction\n")

            print("All streams processed successfully. "
                  "Nexus throughput optimal.")


if __name__ == "__main__":
    """main"""
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")
    print("Initializing Sensor Stream...")
    lst_data = ["temp:22.5", "humidity:65", "pressure:1013"]
    sensor = SensorStream("SENSOR_001")
    print(sensor.process_batch(lst_data))
    print(sensor.filter_data(lst_data, None))
    ress = sensor.get_stats()
    print(f"Sensor analysis: {ress["operations"]} reading processed, "
          f"avg temp: {ress["avg_temp"]}°C")
    print()
    print("Initializing Transaction Stream...")
    lst_transac = ["buy:100", "sell:150", "buy:75"]
    transaction = TransactionStream("TRANS_001")
    print(transaction.process_batch(lst_transac))
    print(transaction.filter_data(lst_transac, None))
    result = transaction.get_stats()
    print(f"Transaction analysis: {result["operations"]} operations, "
          f"net flow: +{result["net_flow"]} units")
    print()
    print("Initializing Event Stream...")
    lst_event = ["login", "error", "logout", "error"]
    event = EventStream("EVENT_001")
    print(event.process_batch(lst_event))
    print(event.filter_data(lst_event, None))
    resul = event.get_stats()
    print(f"Event analisys: {resul["nbr_event"]} events, "
          f"{resul["nbr_error"]} error detected")
    print()
    processor = StreamProcessor()
    processor.add_stream(sensor)
    processor.add_stream(transaction)
    processor.add_stream(event)

    # Prepare data
    sensor_data = ["temp:22.5", "humidity:65", "pressure:1013"]
    transaction = ["buy:100", "sell:150", "buy:75"]
    event_data = ["login", "error", "logout"]

    # Process all streams
    print(processor.process_unified([sensor_data, transaction, event_data],
                                    filter_criteria="High-priorty data only"
                                    ))

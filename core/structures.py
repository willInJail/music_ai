from dataclasses import dataclass, field
from typing import List, Optional, Dict


@dataclass
class Section:
    start_time: float
    end_time: float

    tempo: Optional[float] = None
    time_signature: Optional[str] = None
    key: Optional[str] = None

    metadata: Dict = field(default_factory=dict)

    @property
    def duration(self) -> float:
        return self.end_time - self.start_time


@dataclass
class TrackAnalysis:
    track_path: str
    duration: float
    sample_rate: int

    sections: List[Section] = field(default_factory=list)
    global_features: Dict = field(default_factory=dict)

    def add_section(self, section: Section):
        self.sections.append(section)
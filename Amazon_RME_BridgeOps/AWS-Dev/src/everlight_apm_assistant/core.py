from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Dict, Any


@dataclass
class Header:
    date: str
    site: str = ""
    area: str = ""
    shift: str = ""
    tech_name: str = ""
    manager_on_duty: str = ""
    notes: str = ""


@dataclass
class Item:
    equipment_id: str
    component: str
    action: str
    result: str
    time_spent_min: int = 5
    work_order: str = ""
    notes: str = ""


@dataclass
class Session:
    header: Header
    items: List[Item] = field(default_factory=list)
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())

    def add_item(self, **kwargs) -> None:
        self.items.append(Item(**kwargs))

    def render_text(self) -> str:
        lines = []
        h = self.header
        lines.append(f"Date: {h.date}   Site: {h.site}   Area: {h.area}   Shift: {h.shift}")
        lines.append(f"Tech: {h.tech_name}   MOD: {h.manager_on_duty}")
        if h.notes:
            lines.append(f"Context: {h.notes}")
        lines.append("-" * 72)
        if not self.items:
            lines.append("(No PM items recorded)")
        for i, it in enumerate(self.items, 1):
            tag = f"{i:02d}. {it.equipment_id} | {it.component} | {it.action} -> {it.result} (~{it.time_spent_min}m)"
            if it.work_order:
                tag += f"  WO# {it.work_order}"
            lines.append(tag)
            if it.notes:
                lines.append(f"    Notes: {it.notes}")
        return "\n".join(lines)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "header": self.header.__dict__,
            "items": [i.__dict__ for i in self.items],
            "created_at": self.created_at,
        }
"""Core helpers for EverLight APM assistant - placeholder."""


def process_session(session):
    # placeholder processing
    return {'status': 'ok', 'session_id': session.get('id')}

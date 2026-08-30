"""Two LangGraph memory planes, no model required.

Thread memory (checkpointer): one conversation's graph state, keyed by thread_id.
Long-term memory (store): facts that survive across threads, keyed by namespace + key.

Run from the repo root after `uv sync`:

    uv run python 04-developer/04.1-backend/memory/thread_vs_store.py
"""

from __future__ import annotations

from typing import Annotated, TypedDict

from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph import END, START, StateGraph
from langgraph.graph.message import add_messages
from langgraph.store.memory import InMemoryStore
from langchain_core.messages import HumanMessage


class ThreadState(TypedDict):
    messages: Annotated[list, add_messages]


def echo_turn(state: ThreadState) -> dict:
    last = state["messages"][-1]
    return {"messages": [{"role": "assistant", "content": f"heard: {last.content}"}]}


def build_thread_graph():
    builder = StateGraph(ThreadState)
    builder.add_node("echo", echo_turn)
    builder.add_edge(START, "echo")
    builder.add_edge("echo", END)
    return builder.compile(checkpointer=InMemorySaver())


def demo_thread_memory() -> None:
    graph = build_thread_graph()
    config = {"configurable": {"thread_id": "user-42-chat-1"}}

    graph.invoke({"messages": [HumanMessage("my name is Neeraj")]}, config)
    second = graph.invoke({"messages": [HumanMessage("what is my name?")]}, config)
    history = [m.content for m in second["messages"]]

    other_thread = graph.invoke(
        {"messages": [HumanMessage("what is my name?")]},
        {"configurable": {"thread_id": "user-42-chat-2"}},
    )
    other_history = [m.content for m in other_thread["messages"]]

    print("=== Thread memory (checkpointer) ===")
    print("same thread after two turns:", history)
    print("new thread has no prior turns:", other_history)
    print("checkpoint = this conversation. It does not follow the user to a new thread.")


def demo_store_memory() -> None:
    store = InMemoryStore()
    user_ns = ("user-42", "semantic")
    store.put(user_ns, "name", {"fact": "User's name is Neeraj"})
    store.put(user_ns, "role", {"fact": "Staff security infrastructure engineer"})

    # A different thread still sees the same namespaced facts.
    recalled = store.get(user_ns, "name")
    listed = store.search(user_ns)

    print("=== Long-term memory (store) ===")
    print("get name:", recalled.value if recalled else None)
    print("all facts in namespace:", [item.value for item in listed])
    print("store = user/app facts. Threads are just callers.")


if __name__ == "__main__":
    demo_thread_memory()
    print()
    demo_store_memory()

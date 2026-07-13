"use client";

import { useMemo } from "react";
import {
  Background,
  BackgroundVariant,
  Controls,
  MarkerType,
  Position,
  ReactFlow,
  type Edge as FlowEdge,
  type Node as FlowNode,
} from "@xyflow/react";
import {
  BrainCircuit,
  Network,
  Route,
  Sparkles,
} from "lucide-react";

import type {
  KnowledgeGraph as KnowledgeGraphData,
} from "@/lib/types";

interface KnowledgeGraphProps {
  graph: KnowledgeGraphData;
}

interface DepartmentTone {
  panel: string;
  badge: string;
  dot: string;
}

const DEPARTMENT_TONES: Record<string, DepartmentTone> = {
  it: {
    panel: "border-sky-400/35 bg-sky-500/10",
    badge: "border-sky-400/30 bg-sky-400/10 text-sky-200",
    dot: "bg-sky-400",
  },
  security: {
    panel: "border-rose-400/35 bg-rose-500/10",
    badge: "border-rose-400/30 bg-rose-400/10 text-rose-200",
    dot: "bg-rose-400",
  },
  legal: {
    panel: "border-violet-400/35 bg-violet-500/10",
    badge: "border-violet-400/30 bg-violet-400/10 text-violet-200",
    dot: "bg-violet-400",
  },
  hr: {
    panel: "border-emerald-400/35 bg-emerald-500/10",
    badge: "border-emerald-400/30 bg-emerald-400/10 text-emerald-200",
    dot: "bg-emerald-400",
  },
  finance: {
    panel: "border-amber-400/35 bg-amber-500/10",
    badge: "border-amber-400/30 bg-amber-400/10 text-amber-200",
    dot: "bg-amber-400",
  },
  company: {
    panel: "border-indigo-400/35 bg-indigo-500/10",
    badge: "border-indigo-400/30 bg-indigo-400/10 text-indigo-200",
    dot: "bg-indigo-400",
  },
  general: {
    panel: "border-indigo-400/35 bg-indigo-500/10",
    badge: "border-indigo-400/30 bg-indigo-400/10 text-indigo-200",
    dot: "bg-indigo-400",
  },
  shared: {
    panel: "border-slate-400/30 bg-slate-500/10",
    badge: "border-slate-400/25 bg-slate-400/10 text-slate-200",
    dot: "bg-slate-400",
  },
};

function getDepartmentTone(
  department: string
): DepartmentTone {
  return (
    DEPARTMENT_TONES[department.toLowerCase()] ??
    DEPARTMENT_TONES.shared
  );
}

function normalizeName(value: string): string {
  return value.trim().toLowerCase();
}

function createNodeLabel(
  name: string,
  department: string,
  primary: boolean
) {
  const tone = getDepartmentTone(department);

  return (
    <div
      className={[
        "relative overflow-hidden rounded-2xl border px-4 py-3",
        "shadow-[0_18px_55px_rgba(0,0,0,0.35)] backdrop-blur-xl",
        "transition duration-200 hover:-translate-y-0.5",
        tone.panel,
        primary
          ? "ring-2 ring-indigo-400/70 ring-offset-2 ring-offset-slate-950"
          : "",
      ].join(" ")}
    >
      <div className="flex items-center justify-between gap-3">
        <span className="flex items-center gap-1.5">
          <span
            className={`h-2 w-2 rounded-full shadow-[0_0_14px_currentColor] ${tone.dot}`}
          />
          <span className="text-[9px] font-semibold uppercase tracking-[0.18em] text-slate-400">
            Entity
          </span>
        </span>

        <span
          className={`rounded-full border px-2 py-0.5 text-[9px] font-semibold uppercase tracking-wide ${tone.badge}`}
        >
          {department || "shared"}
        </span>
      </div>

      <p className="mt-2 text-left text-xs font-semibold leading-5 text-slate-100">
        {name}
      </p>

      {primary && (
        <div className="mt-2 flex items-center gap-1 text-[9px] font-medium uppercase tracking-[0.16em] text-indigo-300">
          <Sparkles size={10} />
          Primary concept
        </div>
      )}
    </div>
  );
}

export function KnowledgeGraph({
  graph,
}: KnowledgeGraphProps) {
  const { nodes, edges, signature } = useMemo(() => {
    const centerX = 400;
    const centerY = 190;
    const secondaryCount = Math.max(graph.nodes.length - 1, 1);

    const radiusX =
      graph.nodes.length > 6 ? 330 : 280;

    const radiusY =
      graph.nodes.length > 6 ? 175 : 150;

    const nodeIds = new Map<string, string>();

    const flowNodes: FlowNode[] = graph.nodes.map(
      (node, index) => {
        const id = `kg-node-${index}`;

        if (!nodeIds.has(normalizeName(node.name))) {
          nodeIds.set(normalizeName(node.name), id);
        }

        const primary = index === 0;

        const angle =
          -Math.PI / 2 +
          ((index - 1) / secondaryCount) * Math.PI * 2;

        const position = primary
          ? {
              x: centerX - 95,
              y: centerY - 45,
            }
          : {
              x: centerX + Math.cos(angle) * radiusX - 95,
              y: centerY + Math.sin(angle) * radiusY - 45,
            };

        const leftSide = position.x < centerX;

        return {
          id,
          position,
          sourcePosition: leftSide
            ? Position.Right
            : Position.Left,
          targetPosition: leftSide
            ? Position.Right
            : Position.Left,
          data: {
            label: createNodeLabel(
              node.name,
              node.department,
              primary
            ),
          },
          style: {
            width: 190,
            padding: 0,
            border: "none",
            background: "transparent",
            boxShadow: "none",
          },
        };
      }
    );

    const flowEdges = graph.edges.reduce<FlowEdge[]>(
      (accumulator, edge, index) => {
        const source = nodeIds.get(
          normalizeName(edge.from)
        );

        const target = nodeIds.get(
          normalizeName(edge.to)
        );

        if (!source || !target) {
          return accumulator;
        }

        accumulator.push({
          id: `kg-edge-${index}`,
          source,
          target,
          type: "smoothstep",
          animated: index < 3,
          label: edge.relation,
          markerEnd: {
            type: MarkerType.ArrowClosed,
            color: "#818cf8",
          },
          style: {
            stroke: "#818cf8",
            strokeWidth: 1.7,
          },
          labelStyle: {
            fill: "#cbd5e1",
            fontSize: 10,
            fontWeight: 600,
          },
          labelBgStyle: {
            fill: "#0f172a",
            fillOpacity: 0.94,
          },
          labelBgPadding: [7, 4],
          labelBgBorderRadius: 6,
        });

        return accumulator;
      },
      []
    );

    return {
      nodes: flowNodes,
      edges: flowEdges,
      signature: JSON.stringify(graph),
    };
  }, [graph]);

  if (nodes.length === 0) {
    return null;
  }

  return (
    <section className="mt-5 overflow-hidden rounded-3xl border border-slate-800 bg-slate-950 text-slate-100 shadow-[0_24px_80px_rgba(15,23,42,0.22)]">
      <div className="flex flex-wrap items-center justify-between gap-4 border-b border-slate-800/90 bg-slate-900/70 px-5 py-4 backdrop-blur-xl">
        <div className="flex items-center gap-3">
          <span className="flex h-10 w-10 items-center justify-center rounded-2xl border border-indigo-400/30 bg-indigo-400/10 text-indigo-300 shadow-[0_0_25px_rgba(129,140,248,0.18)]">
            <BrainCircuit size={20} />
          </span>

          <div>
            <div className="flex items-center gap-2">
              <h3 className="text-sm font-semibold text-white">
                Knowledge Graph
              </h3>

              <span className="rounded-full border border-emerald-400/25 bg-emerald-400/10 px-2 py-0.5 text-[9px] font-semibold uppercase tracking-[0.15em] text-emerald-300">
                Live
              </span>
            </div>

            <p className="mt-0.5 text-[11px] text-slate-400">
              Concepts and relationships used to expand the answer
            </p>
          </div>
        </div>

        <div className="flex items-center gap-2 text-[10px] font-medium text-slate-300">
          <span className="flex items-center gap-1.5 rounded-full border border-slate-700 bg-slate-800/70 px-3 py-1.5">
            <Network size={12} />
            {graph.nodes.length} nodes
          </span>

          <span className="flex items-center gap-1.5 rounded-full border border-slate-700 bg-slate-800/70 px-3 py-1.5">
            <Route size={12} />
            {graph.edges.length} links
          </span>
        </div>
      </div>

      <div className="knowledge-flow h-[430px] w-full bg-[radial-gradient(circle_at_center,rgba(79,70,229,0.12),transparent_58%)]">
        <ReactFlow
          key={signature}
          defaultNodes={nodes}
          defaultEdges={edges}
          fitView
          fitViewOptions={{
            padding: 0.18,
            maxZoom: 1.05,
          }}
          minZoom={0.35}
          maxZoom={1.6}
          nodesConnectable={false}
          colorMode="dark"
        >
          <Background
            variant={BackgroundVariant.Dots}
            gap={22}
            size={1.1}
            color="#334155"
          />

          <Controls
            position="bottom-left"
            showInteractive={false}
          />
        </ReactFlow>
      </div>

      {graph.reasoning_path.length > 0 && (
        <div className="border-t border-slate-800 bg-slate-900/55 px-5 py-4">
          <div className="mb-3 flex items-center gap-2">
            <Route size={14} className="text-indigo-300" />
            <p className="text-[10px] font-semibold uppercase tracking-[0.18em] text-slate-400">
              Reasoning paths
            </p>
          </div>

          <div className="grid gap-2 md:grid-cols-2">
            {graph.reasoning_path.map((path, index) => (
              <div
                key={`${path}-${index}`}
                className="flex items-start gap-2 rounded-xl border border-slate-800 bg-slate-950/70 px-3 py-2.5"
              >
                <span className="flex h-5 w-5 shrink-0 items-center justify-center rounded-full bg-indigo-400/10 text-[9px] font-bold text-indigo-300">
                  {index + 1}
                </span>

                <p className="text-[11px] leading-5 text-slate-300">
                  {path}
                </p>
              </div>
            ))}
          </div>
        </div>
      )}
    </section>
  );
}

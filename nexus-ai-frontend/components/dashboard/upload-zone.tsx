"use client";

import { useRef, useState, type DragEvent } from "react";
import { Loader2, UploadCloud } from "lucide-react";
import { cn } from "@/lib/utils";

interface Props {
  onUpload: (file: File) => Promise<void>;
}

export function UploadZone({ onUpload }: Props) {
  const [isDragging, setIsDragging] = useState(false);
  const [isUploading, setIsUploading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const inputRef = useRef<HTMLInputElement>(null);

  const handleFile = async (file: File | undefined) => {
    if (!file) return;
    setError(null);
    setIsUploading(true);
    try {
      await onUpload(file);
    } catch (err) {
      setError(err instanceof Error ? err.message : "Upload failed. Please try again.");
    } finally {
      setIsUploading(false);
    }
  };

  const handleDrop = (e: DragEvent<HTMLDivElement>) => {
    e.preventDefault();
    setIsDragging(false);
    void handleFile(e.dataTransfer.files?.[0]);
  };

  return (
    <div>
      <div
        role="button"
        tabIndex={0}
        onClick={() => inputRef.current?.click()}
        onKeyDown={(e) => {
          if (e.key === "Enter" || e.key === " ") inputRef.current?.click();
        }}
        onDragOver={(e) => {
          e.preventDefault();
          setIsDragging(true);
        }}
        onDragLeave={() => setIsDragging(false)}
        onDrop={handleDrop}
        className={cn(
          "flex cursor-pointer flex-col items-center justify-center gap-2 rounded-xl border border-dashed px-6 py-8 text-center transition-colors",
          isDragging
            ? "border-primary bg-primary/10"
            : "border-border bg-background/30 hover:border-primary/40 hover:bg-accent/10"
        )}
      >
        {isUploading ? (
          <Loader2 size={22} className="animate-spin text-primary" />
        ) : (
          <UploadCloud size={22} className="text-muted-foreground" />
        )}
        <p className="text-sm text-foreground">
          {isUploading ? "Uploading…" : "Drag & drop a document, or click to browse"}
        </p>
        <p className="text-xs text-muted-foreground">PDF, DOCX, or TXT</p>
        <input
          ref={inputRef}
          type="file"
          className="hidden"
          onChange={(e) => void handleFile(e.target.files?.[0])}
        />
      </div>
      {error && <p className="mt-2 text-xs text-destructive">{error}</p>}
    </div>
  );
}

from utils.helpers import call_openai
from textwrap import wrap

class SummaryAgent:
    def __init__(self, transcript_text):
        self.transcript_text = transcript_text
        self.chunk_size = 3000  # ~3000 characters ≈ ~1000 tokens, safe under limit

    def split_transcript(self):
        return wrap(self.transcript_text, self.chunk_size)

    def summarize_chunk(self, chunk):
        prompt = f"Summarize the following part of a YouTube transcript:\n\n{chunk}"
        return call_openai(prompt)

    def summarize(self):
        chunks = self.split_transcript()
        partial_summaries = []

        for i, chunk in enumerate(chunks):
            print(f"\nSummarizing chunk {i+1}/{len(chunks)}...")
            summary = self.summarize_chunk(chunk)
            partial_summaries.append(summary)

        # Final summary synthesis
        combined_summary_prompt = "Combine and polish the following partial summaries into a cohesive final summary:\n\n"
        for idx, s in enumerate(partial_summaries, 1):
            combined_summary_prompt += f"Part {idx}: {s}\n\n"

        print("\nCreating final merged summary...")
        final_summary = call_openai(combined_summary_prompt)
        return final_summary
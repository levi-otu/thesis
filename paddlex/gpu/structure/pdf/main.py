from pathlib import Path
from paddlex import create_pipeline

pipeline = create_pipeline(
        pipeline="./my_path/PP-StructureV3.yaml",
        # use_hpip=True,           # a.k.a. enable_hpi / high-performance inference
        use_tensorrt=True,
        precision="fp16",         # V100 supports fp16 nicely
)

input_file = "../../../../book_of_proof_10.pdf"
output_path = Path("./output")

output = pipeline.predict(
    input=input_file,
    use_doc_orientation_classify=False,
    use_doc_unwarping=False,
    use_textline_orientation=False,
    formulda_recognition_batch_size=12,
    det_limit_side_len=1280,            # a bit larger on GPU for accuracy
    text_recognition_batch_size=64
)

markdown_texts = []
markdown_images = []

for res in output:
    md_info = res.markdown
    markdown_texts.append(md_info)
    markdown_images.append(md_info.get("markdown_images", {}))

# Write the python list to a single string.
try:
    md_text = pipeline.concatenate_markdown_pages(markdown_texts)  # list of page dicts
except AttributeError:
    md_text = "\n\n".join(m.get("markdown_texts", "") for m in markdown_texts)
# md_texts = "\n\n".join(markdown_texts)

mkd_file_path = output_path / f"{Path(input_file).stem}.md"
mkd_file_path.parent.mkdir(parents=True, exist_ok=True)
with open(mkd_file_path, "w", encoding="utf-8") as f:
    f.write(md_text)

for item in markdown_images:
    if item:
        for path, image in item.items():
            file_path = output_path / path
            file_path.parent.mkdir(parents=True, exist_ok=True)
            image.save(file_path)

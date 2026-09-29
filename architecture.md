# Architecture
1. Telemetry layer receives compact endpoint/network event metadata.
2. Feature engine normalizes values and derives behavioural indicators.
3. On-device detector produces a risk score and threat class.
4. Explainability layer records the factors that contributed to the alert.
5. Local response layer shows alerts without uploading raw telemetry.

The prototype uses deterministic scoring for transparency. A future version can replace the scoring function with a quantized ONNX/TFLite model.

"""U6: does Appendix D Sec. 5 hold under appendix_E's architecture (E1, with the relay)?

E1 stands in for code cell 1; E2 and E2b's definitions for Code Cells 2 and 2b; main's
Code Cell D definitions are exec'd on top unchanged. The Sec. 5 report is then diffed
line by line against what main.ipynb stored. Nothing is written back."""
import io, contextlib, nbformat
e = nbformat.read("appendix_E.ipynb", as_version=4)
m = nbformat.read("main.ipynb", as_version=4)
ns = {}
exec(compile(e.cells[2].source, "E1", "exec"), ns)
marker = "evaluation_network = LexicalPredictiveCodingNetwork("
src = e.cells[3].source
exec(compile(src[: src.index(marker)] + "\nevaluation_network = LexicalPredictiveCodingNetwork()\n", "E2", "exec"), ns)
src = e.cells[4].source
exec(compile(src[: src.index("def strong_lambda_comparison")], "E2b", "exec"), ns)
src = m.cells[21].source
exec(compile(src[: src.index("\nappendix_d_report(evaluation_network)")], "D", "exec"), ns)
# Eq. (D5) at the relay: g_S = ell_0 + theta_u r, r = B phi_u (E1's own signature).
class RelayUtilityPlacement(ns["LexicalPredictiveCodingNetwork"]):
    def predict_lexical(self, phi_S):
        return -phi_S
    def predict_state(self, phi_u, theta_u=None, relay=None):
        theta = self.theta_u if theta_u is None else float(theta_u)
        return self.base_log_prior + theta * (self.relay(phi_u) if relay is None else relay)
ns["UtilityPlacementNetwork"] = RelayUtilityPlacement
print("E1 class carries the relay:", hasattr(ns["LexicalPredictiveCodingNetwork"], "relay"))
buf = io.StringIO()
with contextlib.redirect_stdout(buf):
    ns["ell0_placement_report"](ns["evaluation_network"])
under_E1 = buf.getvalue().rstrip("\n").split("\n")
stored = "".join("".join(o.get("text", "")) if isinstance(o.get("text", ""), list) else o.get("text", "")
                 for o in m.cells[21].outputs)
stored = stored[stored.index("  Sec. 5: WHERE ell_0 ENTERS"):].rstrip("\n").split("\n")
diff = [(a, b) for a, b in zip(stored, under_E1) if a != b]
print(f"Sec. 5 lines: stored {len(stored)}, under E1 {len(under_E1)}, differing {len(diff)}")
for a, b in diff[:10]:
    print("  main:", a); print("  E1:  ", b)

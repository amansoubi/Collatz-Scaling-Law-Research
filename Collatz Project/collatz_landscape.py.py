import matplotlib.pyplot as plt
import numpy as np
import os

class CollatzResearcher:
    """
    A professional tool for analyzing the statistical properties 
    of Collatz Conjecture trajectories.
    """

    def __init__(self, output_dir: str):
        self.output_dir = output_dir
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
        print(f"✅ Researcher Initialized. Data will be saved to: {self.output_dir}")

    @staticmethod
    def compute_peak(k: int) -> int:
        """
        Computes the maximum peak of a Collatz trajectory starting from 
        the specific seed n = 3 * (2^k) - 1.
        """
        n = 3 * (2**k) - 1
        max_val = n
        while n > 1:
            if n % 2 == 0:
                n //= 2
            else:
                n = 3 * n + 1
            if n > max_val:
                max_val = n
        return max_val

    def run_landscape_analysis(self, k_start: int, k_end: int):
        """
        Performs the computational sweep and generates the landscape plot.
        """
        k_values = np.arange(k_start, k_end + 1)
        peaks = np.array([self.compute_peak(k) for k in k_values])

        print(f"📊 Computing peaks for k in range [{k_start}, {k_end}]...")
        
        self._plot_landscape(k_values, peaks)
        return k_values, peaks

    def _plot_landscape(self, k_values: np.ndarray, peaks: np.ndarray):
        """
        Generates a publication-quality landscape plot.
        """
        plt.style.use('seaborn-v0_8-muted') # استفاده از استایل حرفه‌ای
        fig, ax = plt.subplots(figsize=(12, 7), dpi=150)

        # رسم خط اصلی و نقاط
        ax.plot(k_values, peaks, color='#2c3e50', linewidth=1.5, alpha=0.8, label='Trajectory Peak')
        ax.scatter(k_values, peaks, color='#e74c3c', s=25, edgecolors='white', zorder=3, label='Peak Points')

        # تنظیمات مقیاس و محورها
        ax.set_yscale('log')
        ax.set_xlabel('Seed Parameter ($k$)', fontsize=13, fontweight='bold')
        ax.set_ylabel('$\max(T(n))$ (Log Scale)', fontsize=13, fontweight='bold')
        ax.set_title('Computational Landscape of Collatz Trajectory Peaks\n'
                     r'Seed Form: $n = 3 \cdot 2^k - 1$', fontsize=15, pad=20)

        # بهبود شبکه (Grid)
        ax.grid(True, which="both", ls="--", alpha=0.4)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)

        ax.legend(frameon=True, loc='upper left')

        # ذخیره‌سازی
        save_path = os.path.join(self.output_dir, "collatz_landscape_pro.png")
        plt.savefig(save_path, bbox_inches='tight')
        print(f"🖼️  Professional plot saved to: {save_path}")
        plt.show()

# --- MAIN EXECUTION BLOCK ---
if __name__ == "__main__":
    # تعیین مسیر خروجی (با استفاده از مسیر تو)
    OUTPUT_PATH = r"C:\Users\efycology\Desktop\Python Projects\Collatz_Analysis"
    
    # ایجاد شیء محقق
    researcher = CollatzResearcher(output_dir=OUTPUT_PATH)
    
    # اجرای تحلیل
    k_start, k_end = 10, 50
    k_vals, peak_vals = researcher.run_landscape_analysis(k_start, k_end)
    
    print("\n✅ Analysis Complete.")

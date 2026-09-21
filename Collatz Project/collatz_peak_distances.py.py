import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

class CollatzDistanceAnalyzer:
    """
    Professional tool to analyze spatial distribution and distances 
    between Collatz peaks in a signal/profile.
    """
    
    def __init__(self, data_array: np.ndarray):
        self.data = data_array
        self.peaks = None
        self.distances = None

    def find_and_analyze(self, height=None, distance=None):
        """
        Detects peaks using SciPy and calculates distance gaps.
        """
        # استفاده از find_peaks برای شناسایی علمی قله‌ها
        self.peaks, _ = find_peaks(self.data, height=height, distance=distance)
        
        # محاسبه فاصله بین قله‌های متوالی (Spacing)
        if len(self.peaks) > 1:
            self.distances = np.diff(self.peaks)
        else:
            self.distances = np.array([])
            
        print(f"✅ Analysis: Found {len(self.peaks)} peaks.")
        return self.peaks, self.distances

    def plot_analysis(self, output_path: str):
        """
        Generates a 2-panel scientific figure (Publication Quality).
        """
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10), dpi=150)
        plt.subplots_adjust(hspace=0.3)

        # پنل اول: پروفایل شدت و نقاط شناسایی شده
        ax1.plot(self.data, color='#1a2a6c', linewidth=1.0, label='Signal Intensity')
        if len(self.peaks) > 0:
            ax1.plot(self.peaks, self.data[self.peaks], "x", color='#e67e22', label='Detected Peaks')
        
        ax1.set_title('Intensity Profile & Detected Peak Sites', fontsize=14, fontweight='bold')
        ax1.set_xlabel('Column Index')
        ax1.set_ylabel('Intensity')
        ax1.grid(True, linestyle='--', alpha=0.6)
        ax1.legend()

        # پنل دوم: توزیع فواصل (Histogram of Distances)
        if len(self.distances) > 0:
            ax2.hist(self.distances, bins=20, color='#f1c40f', edgecolor='black', alpha=0.8)
            ax2.set_title('Distribution of Distances Between Collatz Peaks', fontsize=14, fontweight='bold')
            ax2.set_xlabel('Distance (in pixels/steps)')
            ax2.set_ylabel('Frequency')
        else:
            ax2.text(0.5, 0.5, 'No sufficient peaks detected for distribution analysis', 
                     ha='center', va='center', transform=ax2.transAxes)

        plt.savefig(output_path, bbox_inches='tight')
        print(f"🖼️  Plot saved to: {output_path}")
        plt.show()

# --- مثال عملی برای تست ---
if __name__ == "__main__":
    # ایجاد یک سیگنال نمونه (جایگزین دیتای واقعی خودت کن)
    data = np.random.rand(1000) 
    
    analyzer = CollatzDistanceAnalyzer(data)
    analyzer.find_and_analyze(height=0.8) # پیدا کردن قله‌های بالای مقدار 0.8
    analyzer.plot_analysis("collatz_peak_distances_pro.png")

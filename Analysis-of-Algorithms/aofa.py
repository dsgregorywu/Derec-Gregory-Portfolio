import time
import matplotlib.pyplot as plt
import random
import statistics
import pandas as pd



def time_algorithm(algo, arr):
    start = time.time()
    algo(arr.copy())
    return time.time() - start

def selection_sort(arr):
    # Defines Selection sort, returns the same array passed through
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def merge_sort(arr):
    # Defines Merge sort, returns the same array passed through
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i, j, k = 0, 0, 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def insertion_sort(arr):
    # Defines Insertion sort, returns the same array passed through
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

if __name__ == "__main__":
    import pandas as pd
    sizes = [100, 500, 1000, 5000]
    mergedata = []
    selectiondata = []
    insertiondata = []
    table_data = []
    for size in sizes:
        sel_times = []
        merge_times = []
        insertion_times = []
        for _ in range(5):
            arr = [random.randint(0, 1000) for _ in range(size)]
            sel_times.append(time_algorithm(selection_sort, arr))
            merge_times.append(time_algorithm(merge_sort, arr))
            insertion_times.append(time_algorithm(insertion_sort, arr))
        sel_median = statistics.median(sel_times)
        merge_median = statistics.median(merge_times)
        insertion_median = statistics.median(insertion_times)
        print(f"Size: {size}, Selection Sort Median: {sel_median:.6f}s, Merge Sort Median: {merge_median:.6f}s, Insertion Sort Median: {insertion_median:.6f}s")
        selectiondata.append(sel_median)
        mergedata.append(merge_median)
        insertiondata.append(insertion_median)
        table_data.append({
            'Array Size': size,
            'Selection Sort Median': sel_median,
            'Merge Sort Median': merge_median,
            'Insertion Sort Median': insertion_median
        })

    df = pd.DataFrame(table_data)
    col_map = {
        'Selection Sort Median': 'Selection Sort Median (s)',
        'Merge Sort Median': 'Merge Sort Median (s)',
        'Insertion Sort Median': 'Insertion Sort Median (s)'
    }
    df.rename(columns=col_map, inplace=True)
    df_rounded = df.copy()
    for col in df_rounded.columns:
        if col != 'Array Size':
            df_rounded[col] = df_rounded[col].apply(lambda x: f"{x:.4f}")
    print('\nMedian Times Table:')
    print(df_rounded.to_string(index=False))

    # Show table in a new matplotlib window with improved style
    fig_height = 2 + 0.6 * len(df_rounded)
    fig_table, ax_table = plt.subplots(figsize=(10, fig_height))
    ax_table.axis('off')
    table = ax_table.table(
        cellText=df_rounded.values,
        colLabels=df_rounded.columns,
        cellLoc='center',
        loc='center',
    )
    table.auto_set_font_size(False)
    table.set_fontsize(14)
    table.auto_set_column_width(col=list(range(len(df_rounded.columns))))
    # Style header and rows
    for (row, col), cell in table.get_celld().items():
        if row == 0:
            cell.set_fontsize(15)
            cell.set_text_props(weight='bold', color='#222222')
            cell.set_facecolor('#a7c7e7')
            cell.set_edgecolor('#222222')
            cell.set_linewidth(2)
        elif row % 2 == 1:
            cell.set_facecolor('#e3eafc')
        else:
            cell.set_facecolor('#f8fafc')
        cell.set_edgecolor('#cccccc')
        cell.set_height(0.18)
        cell.PAD = 0.08
    # Center the table vertically
    table.scale(1, 1.3)
    fig_table.suptitle('Median Times Table', fontsize=18, weight='bold', color='#222222', y=0.98)
    plt.subplots_adjust(top=0.85, bottom=0.15)
    plt.show()
    sizes = [100, 500, 1000, 5000]
    mergedata = []
    selectiondata = []
    insertiondata = []
    table_data = []
    for size in sizes:
        sel_times = []
        merge_times = []
        insertion_times = []
        for _ in range(5):
            arr = [random.randint(0, 1000) for _ in range(size)]
            sel_times.append(time_algorithm(selection_sort, arr))
            merge_times.append(time_algorithm(merge_sort, arr))
            insertion_times.append(time_algorithm(insertion_sort, arr))
        sel_median = statistics.median(sel_times)
        merge_median = statistics.median(merge_times)
        insertion_median = statistics.median(insertion_times)
        print(f"Size: {size}, Selection Sort Median: {sel_median:.6f}s, Merge Sort Median: {merge_median:.6f}s, Insertion Sort Median: {insertion_median:.6f}s")
        selectiondata.append(sel_median)
        mergedata.append(merge_median)
        insertiondata.append(insertion_median)
        table_data.append({
            'Array Size': size,
            'Selection Sort Median': sel_median,
            'Merge Sort Median': merge_median,
            'Insertion Sort Median': insertion_median
        })

    df = pd.DataFrame(table_data)
    print('\nMedian Times Table:')
    print(df.to_string(index=False, float_format='%.6f'))
    fig, axs = plt.subplots(1, 2, figsize=(14, 6))
    axs[0].plot(sizes, selectiondata, label='Selection Sort (Median)', color='blue')
    axs[0].plot(sizes, mergedata, label='Merge Sort (Median)', color='red')
    axs[0].plot(sizes, insertiondata, label='Insertion Sort (Median)', color='green')
    axs[0].set_xlabel('Array Size')
    axs[0].set_ylabel('Median Time (seconds)')
    axs[0].set_title('Sorting Algorithm Performance (Median of 5 runs)')
    axs[0].legend()
    axs[1].plot(sizes, selectiondata, label='Selection Sort (Median)', color='blue')
    axs[1].plot(sizes, mergedata, label='Merge Sort (Median)', color='red')
    axs[1].plot(sizes, insertiondata, label='Insertion Sort (Median)', color='green')
    axs[1].set_xlabel('Array Size')
    axs[1].set_ylabel('Median Time (seconds, log scale)')
    axs[1].set_title('Sorting Algorithm Performance (Log-Scale)')
    axs[1].set_yscale('log')
    axs[1].legend()

    plt.tight_layout()
    fig.text(0.5, 0.01, 'Figure: Comparison of sorting algorithm median run times. Left: normal scale. Right: log-scale to show growth rates.', ha='center', fontsize=10)
    plt.show()
